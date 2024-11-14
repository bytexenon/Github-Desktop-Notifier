# GitHub Desktop Notifier

> [!IMPORTANT]  
> This is a Linux-only project.

GitHub Desktop Notifier is a Python script that sends you a desktop notification whenever you receive a notification on GitHub. Stay updated with your GitHub activities without constantly checking your email or GitHub dashboard.

## Features

- **Real-time Notifications**: Get instant desktop notifications for new GitHub activities.
- **Interactive Actions**: Open notifications in your browser or mark them as read directly from the notification popup.
- **Supports All Notification Types**: Receive notifications for issues, pull requests, comments, and more.
- **Easy to Use**: Simply run the script and authenticate with GitHub via browser to start receiving notifications, no need to create GitHub API tokens.

## Preview

![GitHub Desktop Notifier Preview](https://github.com/user-attachments/assets/63951238-ec37-433d-9ec2-aad393e6442e)

## Installation

### Prerequisites

1. **Install required packages**: Install the `libnotify-bin` package to enable desktop notifications on Linux, and the `gh` package to interact with GitHub:

```bash
sudo apt update
sudo apt install libnotify-bin gh
```

2. **Clone the Repository**: Download the script by cloning the repository.

```bash
git clone https://github.com/bytexenon/Github-Desktop-Notifier
cd Github-Desktop-Notifier
```

## Usage

1. **Run the Script**: Start the script to begin receiving notifications.

```bash
python src/__main__.py
```

**That's it!**

If you haven't already authenticated with `gh`, you will be prompted to do so. Follow the printed instructions to authenticate with GitHub. Once you have done so, the script will run in the background and send you notifications for new GitHub activities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
