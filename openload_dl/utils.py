# -*- coding: utf-8 -*-

"""
openload_dl.utils
~~~~~~~~~~~~~~

This module provides utility functions that are used within openload_dl
that are also useful for external consumption.
"""
import os


import requests
from tqdm import tqdm


DEFAULT_CSIZE = 1000 * 1000  # 1MB


def download_file(url, filename=None, csize=DEFAULT_CSIZE, quiet=False):
    """Download file located at `url` and show a progress bar.

    :param url: File's URL.
    :param filename: Optional. Name to use for the file. If not given get the filename from the URL.
    :param csize: Size of download chunks. Defaults to 1MB.
    :param quiet: Boolean. Suppress download's progress output. Defaults to `False`.
    :return: The downloaded file's size in bytes.

    If a file with the same name is already present in the directory assume it
    is a partial download and resume from the last downloaded byte (beware,
    this could cause errors if a different file with the same name is present
    in the directory!).
    """
    r = requests.get(url, stream=True)
    file_size = int(r.headers["Content-Length"])
    if filename is None:
        filename = r.url.split("/")[-1]
    if os.path.exists(filename):
        first_byte = os.path.getsize(
            filename
        )  # TODO: check that this is really a partial download of dlurl's file
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size
    r = requests.get(
        url, headers={"Range": "bytes=%s-%s" % (first_byte, file_size)}, stream=True
    )
    with tqdm(
        total=file_size,
        initial=first_byte,
        unit="B",
        unit_scale=True,
        desc=filename[0:6] + "..." + filename[-7:],  # TODO: Fix bug on short names!
        disable=quiet,
    ) as pbar:
        with open(filename, "ab") as fp:
            for chunk in r.iter_content(chunk_size=csize):
                fp.write(chunk)
                pbar.update(csize)
    return file_size
