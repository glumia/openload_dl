import re

import requests

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

    def __init__(self, chunk_size=DEFAULT_CSIZE):
        """Initialize the downloader and set the default chunk size for the downloads

        :param chunk_size: Downloader chunks size in bytes. Defaults to 1MB.
        """
        self._session = requests.sessions.Session()
        # We have to fake a browser to get valid download urls.
        self._session.headers.update(
            {
                "Host": "openload.co",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.'8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            }
        )
        self.baseurl = "https://openload.co"
        self._chunk_size = chunk_size

    def get_download_url(self, url):
        """Get a download URL for the file to use with a browser/another downloader

        :param url: An openload URL.
        :return: File's download URL.

        The download url for the file isn't contained in the page source but
        loaded asynchronously by some JavaScript code. It sends a request to
        an url and the response is a redirect to a temporary download url
        generated for the user.
        """
        file_id = url.split("/")[
            -2
        ]  # TODO: What if someone passes a shortlink to the file?
        resp = self._session.get(url)
        token = re.search(
            'var suburl = "https:\\\/\\\/thumb.openload.co\\\/externsub\\\/(.*)~"',
            resp.text,
        ).group(1)
        resp = requests.get(
            self.baseurl + "/stream/" + file_id + "~" + token, allow_redirects=False
        )
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
