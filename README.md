openload-dl - Command-line script to download videos from openload inspired to youtube-dl


- [INSTALLATION](#installation)
- [DESCRIPTION](#description)


# Installation

To satisfy the requirements of the script on a Ubuntu system, type:

    sudo apt install chromium-browser
    sudo apt install python3-pip
    sudo pip3 install selenium
    sudo pip3 install requests


# Description
**openload-dl** is a script written in Python to automate the download of videos from openload.co with a simple command-line interface

    openload-dl URL

or with a list of urls

    openload-dl FILE

Example

    ./openload-dl 'https://openload.co/f/UqAeeBcR1-o/myvideo.mp4'
