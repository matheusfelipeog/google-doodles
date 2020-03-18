# -*- coding: utf-8 -*-

# External
import requests
from bs4 import BeautifulSoup

base_url = "https://www.google.com/doodles/"
next_doodle = "hungary-national-day-2020"

while next_doodle != '#':   

    res = requests.get(base_url + next_doodle)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, features='html.parser')

    # Find data in html page -----------
    date = soup.select('#title-card > div > div')[0].get_text()

    title = soup.select('#title-card > div > h2')[0].get_text()

    url_logo = soup.select('#hplogo-img')[0].get('src')

    url_next_doodle = soup.select('#doodle-newer')[0].get('href')

    # Get next doodle for mapping
    if '/doodles/' in url_next_doodle:
        next_doodle = url_next_doodle.split('/')[2]  # Remove o /doodles/ da url.
    else:
        next_doodle = url_next_doodle  # Finish while loop when the character "#" is next url in href.
