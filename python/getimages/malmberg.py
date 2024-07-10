import urllib.request
from os import path
import csv
import io

with open("Malmberg.csv") as fp:
    next(fp)

    data = csv.reader(fp)

    for row in data:
        book_id = row[4]

        if path.isfile(f'docs/{book_id}.pdf'):
            continue

        response = urllib.request.urlopen(
            f"https://view.publitas.com/malmberg/{book_id}/unsupported")

        # A dirty parse but it works
        href = ''
        for line in io.StringIO(response.read().decode("utf-8")).readlines():
            if 'id="open-publication"' not in line:
                continue

            href = line[line.find('href="')+6:line.rfind('"')]

        urllib.request.urlretrieve(
            f"https://view.publitas.com{href}", f'docs/{book_id}.pdf')
