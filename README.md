# openload_dl
A python library and CLI tool which makes easy to download files from openload.co


- [Installation](#Installation)
- [Examples](#Examples)


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

# Examples
## Command-line
    Usage: openload_dl [OPTIONS] [URLS]...
    
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

## Python
    >>> import openload_dl
    >>> oload = openload_dl.OpenloadDownloader()
    >>> oload.get_durl("https://openload.co/f/12345678900/myvideo.mp4")  # Get a download url for the file
    'https://123abcd.oloadcdn.net/dl/l/ism-abc123abc123/12345678900/myvideo.mp4'
    >>> oload.download("https://openload.co/f/12345678900/myvideo.mp4")
    myvideo.mp4:   5%|▌         | 5.00M/96.4M [00:13<03:45, 404kB/s]


