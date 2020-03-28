# -*- coding: utf-8 -*-

# Builtins
import json

# External
import requests

with open('./data/data-google-doodles.json', 'r', encoding='utf-8') as f:
    data_dooodles = json.load(f)

    print('Download initialized. Wait...')
    for year in data_dooodles.keys():

        #TODO: criar diretório para do ano das logos

        for data in data_dooodles[year]:
            url_logo = data['url_logo']

            res = requests.get(url_logo)

            # Download verification
            try:
                res.raise_for_status()
                print(f'File: {data["title"]} - OK')

            except Exception:
                print(f'File: {data["title"]} - Failed')
                continue
