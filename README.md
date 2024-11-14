# GitHub Desktop Notifier

> [!IMPORTANT]  
> This is a Linux-only script. It will not work on Windows or macOS.

GitHub Desktop Notifier is a Python script that sends you a desktop notification whenever you receive a notification on GitHub. Stay updated with your GitHub activities without constantly checking your email or GitHub dashboard.

## Features

- **Real-time Notifications**: Get instant desktop notifications for new GitHub activities.
- **Interactive Actions**: Open notifications in your browser or mark them as read directly from the notification popup.
- **Supports All Notification Types**: Receive notifications for issues, pull requests, comments, and more.

## Preview

![GitHub Desktop Notifier Preview](https://github.com/user-attachments/assets/63951238-ec37-433d-9ec2-aad393e6442e)

## Installation

### Prerequisites

1. **Install `dunstify`**: This package is used to send desktop notifications. You can install it using the following command:

```bash
sudo apt install libnotify-bin
```

2. **Clone the Repository**: Download the script by cloning the repository.

```bash
git clone https://github.com/bytexenon/Github-Desktop-Notifier
cd Github-Desktop-Notifier
```

## Usage

1. **Configure Environment Variables**: Edit the `.env` file in the project directory and add your GitHub username and access token, as shown below:

```properties
GITHUB_TOKEN=your_github_token_here
GITHUB_USER=your_github_username_here
```

2. **Run the Script**: Start the script to begin receiving notifications.

```bash
python .
```

Now it will run in the background and send you a desktop notification whenever you receive a notification on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
