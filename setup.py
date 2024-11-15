# Imports #
from setuptools import setup, find_packages

# Setup #
setup(
    name="github-desktop-notifier",
    version="1.0.0",
    description="Receive instant GitHub notifications on your Linux desktop",
    url="https://github.com/bytexenon/Github-Desktop-Notifier",
    author="bytexenon",
    author_email="ddavi142@asu.edu",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="github desktop notifier linux notifications dunstify gh",
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "github-notifier=github_desktop_notifier.github_desktop_notifier:main",
        ],
    },
)
