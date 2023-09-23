from os import listdir, mkdir, path, remove, rmdir
from urllib.request import urlopen
from io import BytesIO
from loadingbar import bar
from PIL import Image  # pip install Pillow


def noordhoff(url: str) -> list[Image.Image]:
    images: list[Image.Image] = []

    # Cycle through all pages and download them
    for page in bar(range(1, 298)):
        url += str(page) + '.jpg'

        with urlopen(url) as response:
            images.append(Image.open(BytesIO(response.read())))

    # Return the images list
    return images


def jpgtopdf(images: list[Image.Image]) -> None:
    """Converts jpg images to pdf files"""
    if path.isdir('docs'):
        for i in listdir('docs'):
            remove(i)
        rmdir('docs')

    mkdir('docs')

    pdf_path = path.join('.', 'docs', 'document.pdf')

    # Save all the images as a pdf in pdf_path
    images[0].save(
        pdf_path, 'PDF', resolution=100.0, save_all=True, append_images=images[1:]
    )

    if input("Press enter to open document. ") == '':
        from os import system
        from sys import platform

        prefix = 'open ' if platform == 'darwin' \
            else 'exo-open ' if platform == 'linux' \
            else '' if platform == 'win32' else ''

        system(prefix + pdf_path)


if __name__ == '__main__':
    # ges = "https://cdp.contentdelivery.nu/71180ea1-6c83-437a-93b2-9e83bf7f8d01/20181213151352/extract/assets/img/layout/"
    url = "https://cdp.contentdelivery.nu/f1608b21-214a-44a8-b25c-b749c3f33281/20210310142149/extract/assets/img/layout/"
    jpgtopdf(noordhoff(url))
