"""
    GitHub Desktop Notifier
    =======================
    This package acts as a notifier for GitHub notifications on Linux desktops.
    It periodically checks for new notifications and displays them as desktop 
    notifications using `dunstify`. 
    Users can interact with the notifications to open them in a browser or 
    mark them as read.
"""

# Version #
__version__ = "1.0.0"

# Imports #
from github_desktop_notifier import main

# Main #
if __name__ == "__main__":
    main()
