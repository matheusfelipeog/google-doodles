# -*- coding: utf-8 -*-

# External
import requests
from bs4 import BeautifulSoup

# Builtins
import os


def date_format(date: str) -> dict:
    """Formating the date for dict structure

    Example:

        >>> date = date_format("Mai 15, 2015")
        >>> print(date)

        Output: 
            {
                "month": "Mai",
                "day": "15",
                "year": "2015",
                "full_date": "Mai-15-2015"
            }

    @param date -> Date in string format with separator "," between day and year

    @return -> dict structure with month, day, year and full date.
    """

    month, day, year = date.replace(',', '').split(' ')  # Splited date
    full_date = f'{month}-{day}-{year}'

    new_structure = {
        "month": month,
        "day": day,
        "year": year,
        "full_date": full_date
    }

    return new_structure


data = {}

base_url = "https://www.google.com/doodles/"
next_doodle = "burning-man-festival"

while next_doodle != '#':   

    res = requests.get(base_url + next_doodle)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, features='html.parser')

    # Find data in html page -----------

    # Date Structure
    date = date_format(soup.select('#title-card > div > div')[0].get_text())  # Argument is a string

    title = soup.select('#title-card > div > h2')[0].get_text()

    url_logo = soup.select('#hplogo-img')[0].get('src')

    # Get file name in url or create name with title
    file_name = url_logo.split('/')[-1]  
    if not file_name.endswith('.gif') and not file_name.endswith('.jpg'):
        file_name = title.lower().replace(' ', '_') + '.jpg'

    # Get next doodle for mapping
    url_next_doodle = soup.select('#doodle-newer')[0].get('href')
    if '/doodles/' in url_next_doodle:
        next_doodle = url_next_doodle.split('/')[2]  # Remove o /doodles/ da url.
    else:
        next_doodle = url_next_doodle  # Finish while loop when the character "#" is next url in href.
