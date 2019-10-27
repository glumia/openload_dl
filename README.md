# openload_dl
A python library and CLI tool which makes easy to download files from openload.co


- [Installation](#Installation)
- [Description](#Description)


# Installation
Ubuntu or Debian:

    sudo apt install python3-pip
    pip3 install openload_dl


Windows:  
  
Install [Python](https://www.python.org/downloads/) (don't forget to check the "ADD TO PATH" option).
Then open the command prompt and type:

    pip3 install openload_dl
  
On both Ubuntu and Windows:

Download the latest version of [geckodriver](https://github.com/mozilla/geckodriver/releases) ( for Firefox ) or [chromedriver](http://chromedriver.chromium.org/downloads) ( for Chrome ), extract it and add the executable to PATH or put it in the same directory of the script.

[In order for this script to work you need to have [Firefox](https://www.mozilla.org/it/firefox/new/) or [Chrome](https://www.google.com/chrome/) installed on your system.]

# Description

    Usage: openload-dl [OPTIONS] [URLS]...
    
    Options:
      --get-download-url              Extract only file's download url
      --preferred-browser [firefox|chrome]
                                      Select the browser to use  [default:
                                      firefox]
      --no-headless                   Show the browser
      --chunk-size INTEGER            Set the downloader chunk size in bytes
                                      [default: 1000000]
      -q, --quiet                     Don't print download progress information
      --help                          Show this message and exit.




