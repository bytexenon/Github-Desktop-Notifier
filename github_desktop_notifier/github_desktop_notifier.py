# Imports #
import os
import time
import subprocess
import shutil
import threading

from .github import Github
from argparse import ArgumentParser, RawDescriptionHelpFormatter

# Constants #

# Notification urgency levels: low, normal, critical
#  low - The notification is not urgent and can be shown at a lower priority
#  normal - The notification will time out after TIMEOUT_TIME seconds
#  critical - The notification won't time out or be hidden until the user tsakes action
NOTIFICATION_URGENCY = "critical"
REFRESH_RATE = 10  # In seconds
TIMEOUT_TIME = 15  # If urgency is critical, this value is ignored

FILE_PATH = os.path.realpath(__file__)
DIRECTORY_PATH = os.path.dirname(FILE_PATH)
PARENT_DIRECTORY_PATH = os.path.dirname(DIRECTORY_PATH)

GITHUB_ICON_PATH = os.path.join(PARENT_DIRECTORY_PATH, "assets", "github.png")


# GithubDesktopNotifier #
class GithubDesktopNotifier:
    def __init__(self):
        self.github = Github()
        self.read_notifications = []

    def read_arguments(self):
        parser = ArgumentParser(
            description="GitHub Desktop Notifier",
            formatter_class=RawDescriptionHelpFormatter,
        )
        parser.add_argument(
            "--refresh-rate",
            type=int,
            default=REFRESH_RATE,
            help="Interval in seconds to check for new notifications (default: %(default)s)",
        )
        parser.add_argument(
            "--timeout",
            type=int,
            default=TIMEOUT_TIME,
            help="Timeout in seconds for the notification (default: %(default)s). Ignored if urgency is 'critical'.",
        )
        parser.add_argument(
            "--urgency",
            type=str,
            choices=["low", "normal", "critical"],
            default=NOTIFICATION_URGENCY,
            help="Urgency level of the notification: 'low', 'normal', or 'critical' (default: %(default)s)",
        )
        parser.add_argument(
            "--icon-path",
            type=str,
            default=GITHUB_ICON_PATH,
            help="Path to the icon to display in the notification (default: %(default)s)",
        )
        args = parser.parse_args()
        self.refresh_rate = args.refresh_rate
        self.timeout_time = args.timeout
        self.notification_urgency = args.urgency
        self.icon_path = args.icon_path

    def send_notification(
        self,
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
            action_params = [
                "--action=" + f"{value[0]},{value[1]}" for value in actions
            ]
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
                        value[2]()

        threading.Thread(target=_send).start()

    def open_and_mark_as_read(self, url, thread_id):
        os.system(f"xdg-open {url}")
        if not self.github.mark_notification_as_read(thread_id):
            print(f"Failed to mark notification {thread_id} as read")

    def get_detailed_web_url(self, subject_type, api_url, web_url):
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

    def process_notifications(self):
        response = self.github.get_notifications()
        if not response:
            return

        notifications = response
        for notification in notifications:
            thread_id = notification["id"]
            unique_id = f"{thread_id}-{notification['updated_at']}"
            if unique_id in self.read_notifications:
                continue
            self.read_notifications.append(unique_id)
            full_repo_name = notification["repository"]["full_name"]
            notification_reason = notification["reason"]
            subject_type = notification["subject"]["type"]
            web_url = notification["repository"]["html_url"]
            api_url = notification["subject"]["url"]
            web_url = self.get_detailed_web_url(subject_type, api_url, web_url)
            title = f"New {subject_type} notification from {full_repo_name}"
            message = f"Reason: {notification_reason}\nURL: {web_url}"

            print(f"Sending notification: {web_url} [{notification_reason}]")
            self.send_notification(
                title=title,
                message=message,
                appname="Github Notifications",
                timeout=self.timeout_time * 1000,
                urgency=self.notification_urgency,
                icon=self.icon_path,
                actions=[
                    [
                        "open",
                        "Open",
                        lambda: self.open_and_mark_as_read(web_url, thread_id),
                    ],
                    [
                        "markAsRead",
                        "Mark as read",
                        lambda: self.github.mark_notification_as_read(thread_id),
                    ],
                ],
                on_dismissed=lambda: self.github.mark_notification_as_read(thread_id),
                on_expired=lambda: self.github.mark_notification_as_read(thread_id),
            )

    def enter_main_loop(self):
        print("Fetching notifications")
        while True:
            self.process_notifications()
            time.sleep(self.refresh_rate)

    def main(self):
        if shutil.which("dunstify") is None:
            print(
                "dunstify is not installed, please install it before running the script"
            )
            exit(1)
        self.read_arguments()
        self.enter_main_loop()


# Functions #
def main():
    github_desktop_notifier = GithubDesktopNotifier()
    github_desktop_notifier.main()


# Main #
if __name__ == "__main__":
    main()
