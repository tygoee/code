import asyncio

from io import BytesIO
from os import listdir, mkdir, path, remove, rmdir
from PIL import Image
from urllib.request import urlopen
from typing import Any, Callable, Generator

from getch import getch
from loadingbar import bar


async def download_image(url: str, loadingbar: Generator[Any, Any, None]) -> Image.Image:
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


async def noordhoff(base_url: str) -> list[Image.Image]:
    """
    Download images from noordhoff

    :param base_url: The base url
    """

    urls = [
        f"{base_url}{x}.jpg"
        for x in range(1, 298)
    ]

    loadingbar = bar(urls)
    tasks = [download_image(url, loadingbar) for url in urls]

    return await asyncio.gather(*tasks)


def jpgtopdf(images: list[Image.Image]) -> None:
    """
    Converts jpg images to pdf files

    :param images: A list of Pillow images
    """

    if path.isdir('docs'):
        for i in listdir('docs'):
            remove(f'docs/{i}')
        rmdir('docs')

    mkdir('docs')

    pdf_path = path.join('.', 'docs', 'document.pdf')

    # Save all the images as a pdf in pdf_path
    images[0].save(
        pdf_path, 'PDF', resolution=100.0, save_all=True, append_images=images[1:]
    )

    print("Press enter to open the document or any other character to exit. ", end='')
    if getch() == '':
        from os import system
        from sys import platform

        prefix = 'open ' if platform == 'darwin' \
            else 'exo-open ' if platform == 'linux' \
            else '' if platform == 'win32' else ''

        system(prefix + pdf_path)
    else:
        print(end='\n')


if __name__ == '__main__':
    url = "https://cdp.contentdelivery.nu/f1608b21-214a-44a8-b25c-b749c3f33281/20210310142149/extract/assets/img/layout/"
    jpgtopdf(asyncio.run(noordhoff(url)))
