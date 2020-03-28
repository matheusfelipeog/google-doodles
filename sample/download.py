# -*- coding: utf-8 -*-

# Builtins
import json
import os

# External
import requests


def create_logo_file(name: str, response) -> None:
    """Create a new file for logo doodles."""

    with open(os.path.join('.', 'data' , 'logos', name), 'wb') as f:
        for chunk in response.iter_content(100000):
            f.write(chunk)


def main():
    """Run download google doodles."""

    with open(os.path.join('.', 'data', 'data-google-doodles.json'), 'r', encoding='utf-8') as f:
        data_dooodles = json.load(f)

        print('\nDownload initialized. Wait...')
        for year in data_dooodles.keys():

            print(f'Year: {year}')
            for data in data_dooodles[year]:
                url_logo = data['url_logo']

                res = requests.get(url_logo)

                # Download verification
                try:
                    res.raise_for_status()
                    
                    print(f'    File: {data["title"]} - OK')

                except Exception:
                    print(f'    File: {data["title"]} - Failed')
                    continue
            
                create_logo_file(data['file_name'], res)


if __name__ == '__main__':

    if os.path.exists(os.path.join('.', 'data', 'data-google-doodles.json')):
        main()
    else:
        print('Required data-google-doodles.json. Run main.py file.')
