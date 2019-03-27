# row players-wrapper  ## class name which contain all the player names
import os

from selenium import webdriver
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Phantomjs_path = BASE_DIR + '/software/Ubuntu/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
print(Phantomjs_path)

# create a driver
driver = webdriver.PhantomJS(executable_path=Phantomjs_path)

# web page url which should be scrape
url = 'https://www.nba.com/players'

# download the html of that url
driver.get(url)

# print(driver.page_source)  ## For debugging purpose

# create a soup object
soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_='row players-wrapper')

# print(div)  # For debugging purpose

for span_tag in div.find_all('span', class_='name-label'):
    print(span_tag.text)

driver.quit()
