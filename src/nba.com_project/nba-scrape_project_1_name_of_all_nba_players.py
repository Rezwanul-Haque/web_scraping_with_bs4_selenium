from settings.base import PHANTOMJS_PATH, URL
from libray.name import get_nba_player_name, TAG_NAME, TAGS_CLASS_NAME

from selenium import webdriver
from bs4 import BeautifulSoup


# create a driver
driver = webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)

# URL = "" ## if anyone want to overwrite url then un-comment it here and change it

# download the html of that url
driver.get(URL)

# print(driver.page_source)  ## For debugging purpose

PARSER_NAME = 'lxml'  # Very fast, Lenient ## Their are other parsers available

# create a soup object
soup = BeautifulSoup(driver.page_source, PARSER_NAME)

# row players-wrapper  ## class name which contain all the player names
ALL_PLAYERS_TAG_NAME = 'div'
ALL_PLAYERS_TAGS__CLASS_NAME = 'row players-wrapper'

# getting the html div in which all the player names reside
HTML_LIST_DIV = soup.find(ALL_PLAYERS_TAG_NAME, class_=ALL_PLAYERS_TAGS__CLASS_NAME)

# print(div)  # For debugging purpose

TAG_NAME = 'span'
TAGS_CLASS_NAME = 'name-label'

driver.quit()

if __name__ == "__main__":

    nba_player_names = get_nba_player_name(HTML_LIST_DIV, TAG_NAME, TAGS_CLASS_NAME)

    print(nba_player_names)

