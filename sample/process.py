# -*- coding: utf-8 -*-

# @author: Matheus Felipe <github.com/matheusfelipeog>

# External
import requests
from bs4 import BeautifulSoup


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


def start(init: str) -> dict:
    """Function for initialize data download.

    The download takes place from oldest (1998) to newest (presenty).
    To change, enter the selector corresponding to the previous button:

    >>> url_next_doodle = soup.select('#doodle-older')[0].get('href')

    @param init -> URL initial the google doodles.

    @return -> New structure for data google doodles in dict. 
    """

    BASE_URL = "https://www.google.com/doodles/"
    next_doodle = init

    new_data = {}

    print('\nInitialized. This can take a while, wait...')
    while next_doodle != '#':   

        # Creating requests for download the html page -----------

        target_url = BASE_URL + next_doodle
        res = requests.get(target_url)
        res.raise_for_status()

        # HTML parser with BeautifulSoup -----------

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

        # Creating structure of data doodles ------------

        if date['year'] not in new_data.keys():
            new_data[date['year']] = [
                {
                    "title": title,
                    "file_name": file_name,
                    "date": date,
                    "url": target_url,
                    "url_logo": 'https:' + url_logo
                }
            ]
        else:
            new_data[date['year']].append(
                {
                    "title": title,
                    "file_name": file_name,
                    "date": date,
                    "url": target_url,
                    "url_logo": 'https:' + url_logo
                }
            )

        # Get next doodle for mapping
        url_next_doodle = soup.select('#doodle-newer')[0].get('href')
        if '/doodles/' in url_next_doodle:
            next_doodle = url_next_doodle.split('/')[2]  # Remove o /doodles/ da url.
        else:
            next_doodle = url_next_doodle  # Finish while loop when the character "#" is next url in href.

        print(f'Title: {title} [OK]')  # Notify
    
    print('Done...')
    # New structure for data google doodles
    return new_data
