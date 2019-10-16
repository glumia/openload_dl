#!/usr/bin/env python3
"""Usage:
    openload-dl.py [options] URL

Options:
    -e, --extract-dlurl     Extract only file download url
    -o <file>               Download content into <file>
    --chrome                Use chrome browser instead of firefox
    --no-headless           Show the browser
    --chunk-size <csize>    Set the downloader chunk size in
                            bytes (default 1MB
    -h, --help              Print this help and exit
    -v, --version           Print version and exit
"""

import os
import requests
import time
from selenium import webdriver
from tqdm import tqdm
from docopt import docopt

__author__ = "glumia"
__license__ = "GPLv3"
__version__ = "1.1"
__email__ = "gius-italy@live.it"


def close_popups(browser):
    """Close browser's automatically opened popups

    :param browser: An instance of Selenium.webdriver.Firefox or Selenium.webdriver.Chrome
    """
    while len(browser.window_handles) > 1:
        browser.switch_to.window(browser.window_handles[-1])
        browser.close()
    browser.switch_to.window(browser.window_handles[0])


def get_dlurl(url: str, browser) -> str:
    """Extract the direct download url from the openload url

    :param url: An openload video url
    :param browser: An instance of Selenium.webdriver.Firefox or Selenium.webdriver.Chrome
    :return: Video's direct download url
    """
    browser.get(url)
    browser.execute_script("document.getElementById('btnDl').click()")
    close_popups(browser)
    time.sleep(6)
    browser.execute_script("document.getElementById('secondsleftouter').click()")
    close_popups(browser)
    button = browser.find_element_by_css_selector("a.main-button:nth-child(1)")
    dlurl = button.get_attribute("href")
    # We need to override requests default user-agent to avoid bot blocking by openload
    dlurl = requests.get(
        dlurl,
        headers={"User-Agent": browser.execute_script("return navigator.userAgent")},
        allow_redirects=False,
    ).headers["location"]
    return dlurl


def download_file(dlurl: str, filename: str = None, csize: int = 1000 * 1000) -> int:
    """Download direct url's file and show a progress bar

    :param dlurl: Direct url to file
    :param filename: Name to use for the file
    :param csize: Size of download chunks
    :return: The downloaded file's size in bytes
    """
    r = requests.get(dlurl, stream=True)
    file_size = int(r.headers["Content-Length"])
    if filename is None:
        filename = r.url.split("/")[-1]
    if os.path.exists(filename):
        first_byte = os.path.getsize(filename)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size
    r = requests.get(
        dlurl, headers={"Range": "bytes=%s-%s" % (first_byte, file_size)}, stream=True
    )
    with tqdm(
        total=file_size,
        initial=first_byte,
        unit="B",
        unit_scale=True,
        desc=filename[0:6] + "..." + filename[-7:],
    ) as pbar:
        with open(filename, "ab") as fp:
            for chunk in r.iter_content(chunk_size=csize):
                fp.write(chunk)
                pbar.update(csize)
    return file_size


if __name__ == "__main__":
    args = docopt(__doc__, version="openload-dl " + __version__)
    if args["--chunk-size"] is None:
        csize = 1000 * 1000
    else:
        csize = int(args["--chunk-size"])
    if args["--chrome"] is True:
        if args["--no-headless"] is True:
            browser = webdriver.Chrome()
        else:
            chrome_opt = webdriver.ChromeOptions()
            chrome_opt.add_argument("--headless")
            browser = webdriver.Chrome(options=chrome_opt)
    else:
        if args["--no-headless"] is True:
            browser = webdriver.Firefox()
        else:
            fox_opt = webdriver.FirefoxOptions()
            fox_opt.add_argument("--headless")
            browser = webdriver.Firefox(options=fox_opt)
    if args["--extract-dlurl"] is True:
        print(get_dlurl(args["URL"], browser))
        browser.quit()
    else:
        dlurl = get_dlurl(args["URL"], browser)
        browser.quit()
        download_file(dlurl, args["-o"], csize)
    if os.path.exists("geckodriver.log"):
        os.remove("geckodriver.log")
    if os.path.exists("chromedriver.log"):
        os.remove("chromedriver.log")
