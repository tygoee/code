import urllib.request
from os import path, mkdir
import csv
import io

if not path.isdir('docs'):
    mkdir('docs')


with open("Malmberg.csv") as fp:
    next(fp)

    data = csv.reader(fp)

    method = ''
    for row in data:
        method = row[0] if row[0] != '' else method
        book_id = row[4]

        if not path.isdir(f'docs/{method}'):
            mkdir(f'docs/{method}')

        if path.isfile(f'docs/{method}/{book_id}.pdf'):
            continue

        response = urllib.request.urlopen(
            f"https://view.publitas.com/malmberg/{book_id}/unsupported")

        # A dirty parse but it works
        href = ''
        for line in io.StringIO(response.read().decode("utf-8")).readlines():
            if 'id="open-publication"' not in line:
                continue

            href = line[line.find('href="')+6:line.rfind('"')]

        print(book_id)

        urllib.request.urlretrieve(
            f"https://view.publitas.com{href}", f'docs/{method}/{book_id}.pdf')
