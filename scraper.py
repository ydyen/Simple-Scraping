from urllib.request import urlopen
# handles server request to URL

from bs4 import BeautifulSoup
# import web scraping lib

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
# the target web scraping link

soup = BeautifulSoup(html.read(), 'html.parser')
# creates an object for webscraping

# print(soup.prettify()) will print the website html

# divs = soup.find_all('div', {'class': 'featured'}) finds all tags of divs
# divs = soup.find('div', {'class': 'featured'}) #finds div with class and attribute featured

# for div in divs:
# print(divs)

#created an object and assign it to an h2 element
# featured_header_only_h2_element = soup.find('div', {'class': 'featured'}).h2
# print(featured_header_only_h2_element) # prints class featured with child node of h2

# print_text_only = featured_header_only_h2_element.get_text()
# print(print_text_only) #prints class featured with child node of h2 text only **this should be used in the last step in the scraping process

# for button in soup.find(attrs={'class': 'button button--primary'}): #uses attrs keyword search
    #print(button)

# for button in soup.find(class_= 'button button--primary'): #uses class_  keyword search
    #print(button)

# finds all link tags
for link in soup.find_all('a'):
    print(link.get('href')) # prints all links without the a tag
    # print(10*'-')
    # print(link) # prints the link with the a tag