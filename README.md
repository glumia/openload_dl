openload-dl - Command-line script to download videos from openload inspired to youtube-dl


- [Installation](#Installation)
- [Description](#Description)


# Installation
Ubuntu or other unix-lixe systems:

    sudo apt install python3-pip
    pip3 install -r requirements.txt


Windows:  
  
Install [Python](https://www.python.org/downloads/) (don't forget to check the "ADD TO PATH" option).  
Then open the command prompt and type:

    pip3 install -r requirements.txt
  
On both Ubuntu and Windows:  

Download the latest version of [geckodriver](https://github.com/mozilla/geckodriver/releases) ( for Firefox ) or [chromedriver](http://chromedriver.chromium.org/downloads) ( for Chrome ), extract it and add the executable to PATH or put it in the same directory of the script.

[In order for this script to work you need to have [Firefox](https://www.mozilla.org/it/firefox/new/) or [Chrome](https://www.google.com/chrome/) installed on your system.]

# Description
**openload-dl** is a script written in Python to automate the download of videos from openload.co with a simple command-line interface.
    
    Usage:
    openload-dl [options] URL
        
    Options:
        -e, --extract-dlurl     Extract only direct url to file
        -o <file>               Download content into <file>
        --chrome                Use chrome browser instead of firefox
        --no-headless           Show the browser
        --chunk-size <csize>    Set the downloader chunk size in bytes (default 1MB)                     
        -h, --help              Print this help and exit
        -v, --version           Print version and exit


