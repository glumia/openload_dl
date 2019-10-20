# -*- coding: utf-8 -*-

# openload_dl

"""
Openload Downloader
~~~~~~~~~~~~~~~~~~~~~

openload_dl is a python library and CLI tool which makes easy to download files from openload.co

Example usage as Python module:

    >>> import openload_dl
    >>> oload = openload_dl.OpenloadDownloader()
    >>> oload.get_durl("https://openload.co/f/12345678900/myvideo.mp4")  # Get a download url for the file
    'https://123abcd.oloadcdn.net/dl/l/ism-abc123abc123/12345678900/myvideo.mp4'
    >>> oload.download("https://openload.co/f/12345678900/myvideo.mp4")
    myvideo.mp4:   5%|▌         | 5.00M/96.4M [00:13<03:45, 404kB/s]


:copyright: (c) 2019 by Giuseppe Lumia.
:license: MIT License, see LICENSE for more details.
"""
from .__version__ import (
    __title__,
    __description__,
    __version__,
    __author__,
    __author_email__,
    __license__,
    __copyright__,
)
from .openload_dl import OpenloadDownloader
