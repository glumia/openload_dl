import click

from openload_dl.utils import DEFAULT_CSIZE
from .openload_dl import OpenloadDownloader


@click.command()
@click.argument("urls", nargs=-1)
@click.option(
    "--get-download-url",
    is_flag=True,
    default=False,
    help="Extract only file's download url",
)
@click.option(
    "--chunk-size",
    default=DEFAULT_CSIZE,
    show_default=True,
    help="Set the downloader chunk size in bytes",
)
@click.option(
    "-q",
    "--quiet",
    default=False,
    is_flag=True,
    help="Don't print download progress information",
)
def openload_cli(urls, get_download_url, chunk_size, quiet):
    if urls:
        oload = OpenloadDownloader(chunk_size=chunk_size)
        for url in urls:
            if get_download_url:
                print(oload.get_download_url(url))
            else:
                oload.download(url, quiet=quiet)
