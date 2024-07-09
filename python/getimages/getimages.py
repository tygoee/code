import asyncio

from io import BytesIO
from os import path, mkdir
from PIL import Image
from urllib.request import urlopen, HTTPError
from typing import Any, Callable, Generator

from loadingbar import bar
import csv


async def download_image(
        url: str, loadingbar: Generator[Any, Any, None]) -> Image.Image:
    """
    Download image specified with url.

    :param url: The url where it downloads from
    :param loadingbar: The generator function that updates the loading bar
    """

    # Define the return_image lambda function
    return_image: Callable[[str], Image.Image] = (
        lambda url: Image.open(BytesIO(urlopen(url).read())))

    # Download the image
    result = await asyncio.to_thread(lambda: return_image(url))

    # Update the loading bar
    next(loadingbar)

    # Return the image
    return result


async def noordhoff(name: str, base_url: str) -> list[Image.Image]:
    """
    Download images from noordhoff

    :param base_url: The base url
    """

    print(f"Downloading {name} ({url}*.jpg)...")

    def get_pages() -> int:
        """
        Gets the amount of pages with a binary search
        """

        low, high = 1, 500

        while low < high:
            mid = (low + high + 1) // 2
            res: int

            try:
                res = urlopen(f"{base_url}{mid}.jpg").getcode()
            except HTTPError as e:
                res = e.code

            if res == 404:
                high = mid - 1
            else:
                low = mid

        return low

    urls = [
        f"{base_url}{x}.jpg"
        for x in range(1, get_pages() + 1)
    ]

    loadingbar = bar(urls)
    tasks = [download_image(url, loadingbar) for url in urls]

    return await asyncio.gather(*tasks)


def jpgtopdf(name: str, images: list[Image.Image]) -> None:
    """
    Converts jpg images to pdf files

    :param images: A list of Pillow images
    """

    if not path.isdir('docs'):
        mkdir('docs')

    pdf_path = path.join('.', 'docs', name + '.pdf')

    if len(images) < 1:
        raise FileNotFoundError(f"{name} was not found")

    # Save all the images as a pdf in pdf_path
    images[0].save(
        pdf_path, 'PDF', resolution=100.0,
        save_all=True, append_images=images[1:]
    )

    print("Download complete.\n")


if __name__ == '__main__':
    with open('Noordhoff.csv', 'r') as fp:
        next(fp)

        data = csv.reader(fp)

        for row in data:
            name = row[5].replace('/', '-')  # For file names
            ebookid = row[6] if not row[8] else row[8]
            timestamp = row[7]

            url = f"https://cdp.contentdelivery.nu/{ebookid}/" \
                f"{timestamp}/extract/assets/img/layout/"

            jpgtopdf(name, asyncio.run(noordhoff(name, url)))
