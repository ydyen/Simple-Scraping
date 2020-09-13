from bs4 import BeautifulSoup
from selenium import webdriver

import time

#uses the chrome browser
driver = webdriver.Chrome()

#target link to be test
driver.get('https://treehouse-projects.github.io/horse-land/index.html')
time.sleep(5)

#gets the source code of the index.html page when it was open or read
page_html = driver.page_source

soup = BeautifulSoup(page_html, 'html.parser')
print(soup.prettify())

driver.close()