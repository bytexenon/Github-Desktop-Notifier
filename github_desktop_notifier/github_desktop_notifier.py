# Imports #
import os
import time
import subprocess
import shutil
import threading

from .github import Github

# Constants #

# Notification urgency levels: low, normal, critical
#  low - The notification is not urgent and can be shown at a lower priority
#  normal - The notification will time out after TIMEOUT_TIME seconds
#  critical - The notification won't time out or be hidden until the user takes action
NOTIFICATION_URGENCY = "critical"
REFRESH_RATE = 10  # In seconds
TIMEOUT_TIME = 15  # If urgency is critical, this value is ignored

FILE_PATH = os.path.realpath(__file__)
DIRECTORY_PATH = os.path.dirname(FILE_PATH)
PARENT_DIRECTORY_PATH = os.path.dirname(DIRECTORY_PATH)

GITHUB_ICON_PATH = os.path.join(PARENT_DIRECTORY_PATH, "assets", "github.png")

# Variables #
read_notifications = []


# Functions #
def send_notification(
    title,
    message,
    appname,
    timeout=5000,
    urgency="normal",
    actions=[],
    icon=None,
    on_expired=None,
    on_dismissed=None,
):
    def _send():
        action_params = ["--action=" + f"{value[0]},{value[1]}" for value in actions]
        result = subprocess.run(
            [
                "dunstify",
                title,
                message,
                f"--timeout={timeout}",
                f"--urgency={urgency}",
                f"--icon={icon}",
                f"--appname={appname}",
                *action_params,
            ],
            capture_output=True,
            text=True,
        )

        action = result.stdout.strip()
        if action == "1" and on_expired is not None:
            print("Notification expired")
            on_expired()
        elif action == "2" and on_dismissed is not None:
            print("Notification dismissed")
            on_dismissed()
        else:
            for value in actions:
                if action == value[0]:
                    value[2]()  # Call the function

    threading.Thread(target=_send).start()


def open_and_mark_as_read(github, url, thread_id):
    os.system(f"xdg-open {url}")
    if not github.mark_notification_as_read(thread_id):
        print(f"Failed to mark notification {thread_id} as read")


def get_detailed_web_url(subject_type, api_url, web_url):
    if subject_type == "Issue":
        issue_number = api_url.split("/")[-1]
        web_url = f"{web_url}/issues/{issue_number}"
    elif subject_type == "PullRequest":
        pr_number = api_url.split("/")[-1]
        web_url = f"{web_url}/pull/{pr_number}"
    elif subject_type == "Commit":
        commit_sha = api_url.split("/")[-1]
        web_url = f"{web_url}/commit/{commit_sha}"
    elif subject_type == "Discussion":
        discussion_number = api_url.split("/")[-1]
        web_url = f"{web_url}/discussions/{discussion_number}"
    elif subject_type == "Release":
        release_tag = api_url.split("/")[-1]
        web_url = f"{web_url}/releases/tag/{release_tag}"
    return web_url


def process_notifications(github):
    response = github.get_notifications()
    if not response:
        return

    notifications = response
    for notification in notifications:
        thread_id = notification["id"]
        unique_id = f"{thread_id}-{notification['updated_at']}"
        if unique_id in read_notifications:
            print(f"Notification {unique_id} already read")
            continue
        read_notifications.append(unique_id)
        full_repo_name = notification["repository"]["full_name"]
        notification_reason = notification["reason"]
        subject_type = notification["subject"]["type"]
        web_url = notification["repository"]["html_url"]
        api_url = notification["subject"]["url"]
        web_url = get_detailed_web_url(subject_type, api_url, web_url)
        title = f"New {subject_type} notification from {full_repo_name}"
        message = f"Reason: {notification_reason}\nURL: {web_url}"

        print(f"Sending notification: {web_url} [{notification_reason}]")
        send_notification(
            title=title,
            message=message,
            appname="Github Notifications",
            timeout=TIMEOUT_TIME * 1000,
            urgency=NOTIFICATION_URGENCY,
            icon=GITHUB_ICON_PATH,
            actions=[
                [
                    "open",
                    "Open",
                    lambda: open_and_mark_as_read(github, web_url, thread_id),
                ],
                [
                    "markAsRead",
                    "Mark as read",
                    lambda: github.mark_notification_as_read(thread_id),
                ],
            ],
            on_dismissed=lambda: github.mark_notification_as_read(thread_id),
            on_expired=lambda: github.mark_notification_as_read(thread_id),
        )


def main_loop(github):
    print("Fetching notifications")
    while True:
        process_notifications(github)
        time.sleep(REFRESH_RATE)


def main():
    # Check if command "dunstify" is available
    if shutil.which("dunstify") is None:
        print("dunstify is not installed, please install it before running the script")
        exit(1)

    # Start the main loop
    github = Github()
    main_loop(github)


# Main #
if __name__ == "__main__":
    main()
