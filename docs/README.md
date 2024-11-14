# GitHub Desktop Notifier

[![License](https://img.shields.io/github/license/bytexenon/Github-Desktop-Notifier)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/bytexenon/Github-Desktop-Notifier)](https://github.com/bytexenon/Github-Desktop-Notifier/stargazers)

**GitHub Desktop Notifier** is an easy-to-use Python script that sends you a desktop notification whenever you receive a notification on GitHub. Stay updated with your GitHub activities without constantly checking your email or GitHub dashboard. Get instant desktop notifications for new issues, pull requests, comments, and more.

## Features

- **Real-time Notifications**: Receive instant desktop alerts for new GitHub activities.
- **Interactive Actions**: Open notifications in your browser or mark them as read directly from the notification popup.
- **Supports All Notification Types**: Get notifications for issues, pull requests, comments, and more.
- **Easy to Use**: Simply run the script and authenticate with GitHub via browser to start receiving notifications, no need to create GitHub API tokens.

## Preview

![GitHub Desktop Notifier Preview](https://github.com/user-attachments/assets/63951238-ec37-433d-9ec2-aad393e6442e)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3**: The script is written in Python and requires Python 3 to run.
- **libnotify-bin**: Enables desktop notifications on Linux systems.
- **GitHub CLI (`gh`)**: Allows the script to interact with GitHub.

**Install required packages on Debian/Ubuntu:**

```bash
sudo apt update
sudo apt install -y python3 libnotify-bin gh
```

2. **Clone the Repository**: Download the script by cloning the repository.

```bash
git clone https://github.com/bytexenon/Github-Desktop-Notifier
cd Github-Desktop-Notifier
```

## Usage

Using GitHub Desktop Notifier is straightforward. Follow these steps to start receiving notifications:

1. **Run the Script**: Start the script to begin receiving notifications.

```bash
python src/__main__.py
```

- If you haven't authenticated with `gh` (GitHub CLI), you'll be prompted to do so. Follow the instructions to authenticate via your web browser.
- After authenticating, the script will run in the background and send you desktop notifications for new GitHub activities.

**That's it!** You'll now receive desktop notifications for new GitHub activities. Click on the notification buttons to open the notification in your browser or mark it as read.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
