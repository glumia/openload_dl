openload-dl - Command-line script to download videos from openload inspired to youtube-dl


- [INSTALLATION](#installation)
- [DESCRIPTION](#description)


# Installation

To satisfy the requirements of the script on a Ubuntu system, type:

    sudo apt-get install python3-pip
    sudo apt-get install xvfb
    sudo pip3 install selenium
    sudo pip3 install pyvirtualdisplay
    sudo pip3 install requests

Then download the latest release of geckodriver compatible with your system from https://github.com/mozilla/geckodriver/releases, extract the archive and put the executable in /usr/local/bin



# Description
**openload-dl** is a script written in Python which uses selenium and virtual displays to automate the download of videos from openload.co through the use of a simple command.

    openload-dl URL

or with a list of urls

    openload-dl FILE

Example

    ./openload-dl 'https://openload.co/f/UqAeeBcR1-o/myvideo.mp4'
