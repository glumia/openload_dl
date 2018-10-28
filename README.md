openload-dl - Command-line script to download videos from openload inspired to youtube-dl


- [INSTALLATION](#installation)
- [DESCRIPTION](#description)


# Installation

To satisfy the requirements of the script on a Ubuntu system, type:

    sudo apt install python3-pip
    sudo pip3 install selenium
    sudo pip3 install requests

You'll also need Firefox or Chrome browser, so if neither of the two is installed on you system just type:

    sudo apt install firefox
or

    sudo apt install chromium-browser


On Windows:
- Install [Python](https://www.python.org/downloads/) (don't forget to check the "ADD TO PATH" option)
- Install [Firefox](https://www.mozilla.org/it/firefox/) or [Chrome](https://www.google.com/chrome/)

Then open the command prompt and type:

    pip3 install selenium
    pip3 install requests


On both Ubuntu and Windows: 

Download the latest version of [geckodriver](https://github.com/mozilla/geckodriver/releases) ( for Firefox ) or [chromedriver](http://chromedriver.chromium.org/downloads) ( for Chrome ), extract it and put the executable in the same directory of the script.  



## Setting Chrome instead of Firefox ## 
By default the script works with Firefox. If you want to use Chrome: open the source code with a text editor, comment lines 23,24 and 29 putting a '#' at the beginning and remove the '#' on lines 25,26,30. 




# Description
**openload-dl** is a script written in Python to automate the download of videos from openload.co with a simple command-line interface

    openload-dl URL

or with a list of urls

    openload-dl FILE

Example

    ./openload-dl 'https://openload.co/f/UqAeeBcR1-o/myvideo.mp4'

On Windows

    python openload-dl 'https://openload.co/f/UqAeeBcR1-o/myvideo.mp4'

To set a folder everything sould be downloaded to, specify the folder as second argument.

    openload-dl URL FOLDER

or with a list of urls

    openload-dl FILE FOLDER

Example

    ./openload-dl 'https://openload.co/f/UqAeeBcR1-o/myvideo.mp4' './myvids/'

On Windows

    python openload-dl 'https://openload.co/f/UqAeeBcR1-o/myvideo.mp4' './myvids/'

