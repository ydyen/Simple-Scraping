from urllib.request import urlopen
from bs4 import BeautifulSoup

import re
site_links = []
html = urlopen('https://treehouse-projects.github.io/horse-land/')
soup = BeautifulSoup(html, 'html.parser')


def internal_links(linkURL):
    return soup.find('a', href=re.compile('(.html)$'))


def external_links(linkURL):
    for link in soup.find_all(linkURL):
        print (link.get('href'))


if __name__ == '__main__':
    urls = internal_links('index.html')
    try:
        while len(urls) > 0:
            page = urls.attrs['href']
            if page not in site_links:
                site_links.append(page)

                print(page)
                print('\n============\n')
                urls = internal_links(page)
            else:
                break
    except TypeError:
        print("There is a type error!")
    except NameError:
        print("There was a NameError!")

external_links('a')


