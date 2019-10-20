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
    "--preferred-browser",
    type=click.Choice(["firefox", "chrome"], case_sensitive=False),
    default="firefox",
    show_default=True,
    help="Select the browser to use",
)
@click.option("--no-headless", default=False, is_flag=True, help="Show the browser")
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
def openload_cli(
    urls, get_download_url, preferred_browser, no_headless, chunk_size, quiet
):
    if urls:
        oload = OpenloadDownloader(preferred_browser, not no_headless, chunk_size)
        for url in urls:
            if get_download_url:
                print(oload.get_download_url(url))
            else:
                # TODO: Handle Control+C (SIGINT)
                oload.download(url, quiet=quiet)
