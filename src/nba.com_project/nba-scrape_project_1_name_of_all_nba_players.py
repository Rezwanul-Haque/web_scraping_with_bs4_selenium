import sys
sys.path.append("..")

from bs4 import BeautifulSoup

from library import CreatePhantomjsDriver
from library.nba.name import get_nba_player_name, TAG_NAME, TAGS_CLASS_NAME
from settings.base import PHANTOMJS_PATH, URL


# Constants
# URL = "" ## if anyone want to overwrite url then un-comment it here and change it
# row players-wrapper  ## class name which contain all the player names
ALL_PLAYERS_TAG_NAME = 'div'
ALL_PLAYERS_TAGS__CLASS_NAME = 'row players-wrapper'
TAG_NAME = 'span'
TAGS_CLASS_NAME = 'name-label'
# Constants end

# create a phantom js driver
driver = CreatePhantomjsDriver(PHANTOMJS_PATH)

# download the html of that url
driver.get(URL)

# print(driver.page_source)  ## For debugging purpose

# create a soup object
soup = BeautifulSoup(driver.page_source, PARSER_NAME)

# getting the html div in which all the player names reside
html_div_of_player_names = soup.find(ALL_PLAYERS_TAG_NAME, class_=ALL_PLAYERS_TAGS__CLASS_NAME)

# print(div)  # For debugging purpose

nba_player_names = get_nba_player_name(html_div_of_player_names, TAG_NAME, TAGS_CLASS_NAME)

driver.quit()

if __name__ == "__main__":
    for player_name in nba_player_names:
        print(player_name)

