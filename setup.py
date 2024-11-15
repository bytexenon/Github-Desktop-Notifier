# Imports #
import os

from setuptools import setup, find_packages

# Constants #
DIRNAME = os.path.dirname(__file__)
SHORT_DESCRIPTION = "Receive instant GitHub notifications on your Linux desktop"
LONG_DESCRIPTION = open(os.path.join(DIRNAME, "docs", "README.md")).read()

__version__ = "1.0.0"

# Setup #
setup(
    name="github-desktop-notifier",
    version=__version__,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/bytexenon/Github-Desktop-Notifier",
    author="bytexenon",
    author_email="ddavi142@asu.edu",
    license="MIT",
    python_requires=">=3.6",
    include_package_data=True,
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
    project_urls={
        "Documentation": "https://github.com/bytexenon/Github-Desktop-Notifier",
        "Source": "https://github.com/bytexenon/Github-Desktop-Notifier",
        "Tracker": "https://github.com/bytexenon/Github-Desktop-Notifier/issues",
        "Changelog": "https://github.com/bytexenon/Github-Desktop-Notifier/releases",
    },
    keywords="github desktop notifier linux notifications dunstify gh",
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "github-notifier=github_desktop_notifier.github_desktop_notifier:main",
        ],
    },
)
