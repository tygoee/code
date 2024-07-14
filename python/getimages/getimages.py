import asyncio

from io import BytesIO
from os import path, mkdir
from PIL import Image
from urllib.request import urlopen, HTTPError
from typing import Any, Callable, Generator

from loadingbar import bar
import csv


class Noordhoff:
    def __init__(self, file: str):
        for name, url in self.load_csv(file):
            # Skip if file is already downloaded
            if path.isfile(f"docs/{name}.pdf"):
                continue

            self.loadingbar: Generator[Any, Any, None]
            self.name = name
            self.url = url

            self.jpgtopdf(asyncio.run(self.download_images()))

    async def download_image(self, url: str) -> Image.Image:
        """
        Download image specified with url.

        :param url: The url where it downloads from
        """

        # Define the return_image lambda function
        return_image: Callable[[str], Image.Image] = (
            lambda url: Image.open(BytesIO(urlopen(url).read())))

        # Download the image
        result = await asyncio.to_thread(lambda: return_image(url))

        # Update the loading bar
        next(self.loadingbar)

        # Return the image
        return result

    async def download_images(self) -> list[Image.Image]:
        """
        Download images from noordhoff

        :param base_url: The base url
        """

        print(f"Downloading {self.name}... ({self.url}*.jpg)")

        def get_pages() -> int:
            """
            Gets the amount of pages with a binary search
            """

            low, high = 1, 500

            while low < high:
                mid = (low + high + 1) // 2
                res: int

                try:
                    res = urlopen(f"{self.url}{mid}.jpg").getcode()
                except HTTPError as e:
                    res = e.code

                if res == 404:
                    high = mid - 1
                else:
                    low = mid

            return low

        urls = [
            f"{self.url}{x}.jpg"
            for x in range(1, get_pages() + 1)
        ]

        self.loadingbar = bar(urls)
        tasks = [self.download_image(url) for url in urls]

        return await asyncio.gather(*tasks)

    def jpgtopdf(self, images: list[Image.Image]) -> None:
        """
        Converts jpg images to pdf files

        :param images: A list of Pillow images
        """

        # Create docs directory
        if not path.isdir('docs'):
            mkdir('docs')

        pdf_path = path.join('.', 'docs', self.name + '.pdf')

        if len(images) < 1:
            raise FileNotFoundError(f"{self.name} was not found")

        # Save all the images as a pdf in pdf_path

        # TODO: Organize by folder (with method as foldername)
        images[0].save(
            pdf_path, 'PDF', resolution=100.0,
            save_all=True, append_images=images[1:]
        )

        print("Download complete.\n")

    def load_csv(self, file: str) -> Generator[tuple[str, str], None, None]:
        with open(file, 'r') as fp:
            next(fp)  # Skip the first line

            data = csv.reader(fp)

            for row in data:
                name = row[5].replace('/', '-')  # For file names
                ebookid = row[6] if not row[8] else row[8]
                timestamp = row[7]

                url = f"https://cdp.contentdelivery.nu/{ebookid}/" \
                    f"{timestamp}/extract/assets/img/layout/"

                yield name, url


if __name__ == '__main__':
    Noordhoff('Noordhoff.csv')
