# Imports #
import subprocess
import shutil
import json


# Response #
class Response:
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.text = message

    def __str__(self):
        return f"Status Code: {self.status_code}, Text: {self.text}"


# Github #
class Github:
    """
    A wrapper around the `gh` command-line tool for interacting with GitHub.
    """

    def __init__(self):
        self._validate_installation()
        self._validate_credentials()

    def _run_command(self, *args, **kwargs):
        try:
            result = subprocess.run(
                ["gh", *args],
                capture_output=True,
                text=True,
                check=True,
                **kwargs,
            )
            return result
        except subprocess.CalledProcessError as e:
            print(f"Failed to run command: {e}")
            return None

    def _api_call(self, *args, **kwargs):
        result = self._run_command("api", *args, **kwargs)
        response = Response(1, "[]") if result == None else Response(0, result.stdout)
        return response

    def _validate_installation(self):
        if shutil.which("gh") is None:
            raise RuntimeError("The `gh` command-line tool is not installed.")

    def _validate_credentials(self):
        output = self._run_command("auth", "status").stdout
        if "Logged in to github.com account" not in output:
            answer = input("Would you like to log in to GitHub? (Y/n): ")
            if answer.lower() in ["y", "yes", ""]:
                self._login_if_needed()
            else:
                raise RuntimeError("You must be logged in to GitHub.")

    def _login_if_needed(self):
        self._run_command("auth", "login", "--web", "--git-protocol=HTTPS")

    def get_notifications(self):
        response = self._api_call("notifications")
        if response.status_code == 0:
            return json.loads(response.text)
        return None

    def mark_notification_as_read(self, thread_id):
        response = self._api_call(
            f"notifications/threads/{thread_id}", "--method=PATCH"
        )
        return response.status_code == 0
