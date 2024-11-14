# Imports #
import requests
from requests.auth import HTTPBasicAuth


# Github #
class Github:
    def __init__(self, token, username):
        self.token = token
        self.username = username
        self._validate_credentials()
        print("Successfully authenticated with GitHub")

    def _request(self, method, url, headers, data=None):
        return requests.request(
            method,
            url,
            headers=headers,
            auth=HTTPBasicAuth(self.username, self.token),
            data=data,
        )

    def _validate_credentials(self):
        url = "https://api.github.com/user"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = self._request("GET", url, headers)
        if response.status_code != 200:
            raise ValueError("Invalid GitHub token or username")

    def get_notifications(self):
        url = "https://api.github.com/notifications"
        headers = {"Accept": "application/vnd.github.v3+json"}
        request = self._request("GET", url, headers)
        if request.status_code != 200:
            print("Failed to get notifications")
            print(request.text)
        return request

    def mark_notification_as_read(self, thread_id):
        url = f"https://api.github.com/notifications/threads/{thread_id}"
        headers = {"Accept": "application/vnd.github.v3+json"}
        request = self._request("PATCH", url, headers)
        if request.status_code != 205:
            print(f"Failed to mark notification {thread_id} as read")
            print(request.text)
        return request
