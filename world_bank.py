# Get country data from World Bank API
# Scrape result page to get name and income level of country

from urllib.request import urlopen
from bs4 import BeautifulSoup

import csv


def get_country(country_code):
    html = urlopen('http://api.worldbank.org/v2/countries/{}'
                   .format(country_code))
    soup = BeautifulSoup(html, 'xml')
    country_name = soup.find('wb:name')
    region = soup.find('wb:region')
    income_level = soup.find('wb:incomeLevel')

    print(country_name.get_text())
    print(region.get_text())
    print(income_level.get_text())


if __name__ == '__main__':
    file = open('country_iso_codes.csv', 'r')
    reader = csv.reader(file, delimiter=',')
    for code in reader:
        print(code)
        get_country(code[0])
