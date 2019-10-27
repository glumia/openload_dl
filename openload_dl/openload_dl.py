import os

import requests
from selenium import webdriver

from openload_dl.utils import download_file, DEFAULT_CSIZE


class OpenloadDownloader(object):
    """An Openload downloader.

    Basic Usage::

      >>> import openload_dl
      >>> oload = openload_dl.OpenloadDownloader()
      >>> oload.get_download_url("https://openload.co/f/12345678900/myvideo.mp4")
      'https://123abcd.oloadcdn.net/dl/l/ism-abc123abc123/12345678900/myvideo.mp4'
      >>> oload.download("https://openload.co/f/12345678900/myvideo.mp4")
      myvideo.mp4:   5%|▌         | 5.00M/96.4M [00:13<03:45, 404kB/s]
    """

    def __init__(
        self, preferred_browser="firefox", headless=True, chunk_size=DEFAULT_CSIZE
    ):
        """Initialize the downloader and set the default chunk size for the downloads

        :param preferred_browser: "firefox" or "chrome". Browser to use for the downloader. Defaults to "firefox".
        :param headless: Boolean. Hide/show the browser. Defaults to `True`.
        :param chunk_size: Downloader chunks size in bytes. Defaults to 1MB.
        """
        self.baseurl = "https://openload.co"
        self._chunk_size = chunk_size
        # TODO: check if chromedriver/geckodriver is already present, eventually ask the user if he wants the
        #  script to download it
        if preferred_browser == "firefox":
            if headless:
                fox_opt = webdriver.FirefoxOptions()
                fox_opt.add_argument("--headless")
                self._browser = webdriver.Firefox(options=fox_opt)
            else:
                self._browser = webdriver.Firefox()
        if preferred_browser == "chrome":
            if headless:
                chrome_opt = webdriver.ChromeOptions()
                chrome_opt.add_argument("--headless")
                self._browser = webdriver.Chrome(options=chrome_opt)
            else:
                self._browser = webdriver.Chrome()

    def __del__(self):
        """Close selenium webdriver and delete logs.
        """
        # TODO: configure selenium's webdriver to not generate the log files in __init__ and remove this code
        if os.path.exists("geckodriver.log"):
            os.remove("geckodriver.log")
        if os.path.exists("chromedriver.log"):
            os.remove("chromedriver.log")
        self._browser.quit()

    def _close_popups(self):
        """Close browser's automatically opened popups.
        """
        while len(self._browser.window_handles) > 1:
            self._browser.switch_to.window(self._browser.window_handles[-1])
            self._browser.close()
        self._browser.switch_to.window(self._browser.window_handles[0])

    def get_download_url(self, url):
        """Get a download URL for the file to use with a browser/another downloader

        :param url: An openload URL.
        :return: File's download URL.

        The download url for the file isn't contained in the page source but
        loaded asynchronously by some JavaScript code. It sends a request to
        an url and the response is a redirect to a temporary download url
        generated for the user.
        """
        self._browser.get(url)
        self._close_popups()
        dl_path = self._browser.find_element_by_css_selector(
            "#DtsBlkVFQx"
        ).get_attribute("textContent")
        resp = requests.get(self.baseurl + "/stream/" + dl_path, allow_redirects=False)
        return resp.headers["location"]

    def download(self, url, filename=None, csize=None, quiet=False):
        """Download the file and save it as `filename` if this argument is given.

        :param url: An openload URL.
        :param filename: Optional. If not given get the filename from the URL.
        :param csize: Optional. If not given use `self._chunk_size`.
        :param quiet: Boolean. Suppress download's progress output. Defaults to `False`.
        """
        if csize is None:
            csize = self._chunk_size
        download_url = self.get_download_url(url)
        download_file(download_url, filename, csize, quiet)
