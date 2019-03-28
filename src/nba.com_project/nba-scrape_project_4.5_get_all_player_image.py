import sys
import requests
sys.path.append("..")

from bs4 import BeautifulSoup
from settings.base import PHANTOMJS_PATH, URL, PARSER_NAME
from library.drivers import CreatePhantomjsDriver
from library.nba.name import get_nba_player_name_and_detail_link, TAG_NAME, TAGS_CLASS_NAME
from library.nba.images import get_nba_player_images


# Constants
# URL = "" ## if anyone want to overwrite url then un-comment it here and change it
# row players-wrapper  ## class name which contain all the player names
ALL_PLAYERS_TAG_NAME = 'div'
ALL_PLAYERS_TAGS__CLASS_NAME = 'row players-wrapper'
TAG_NAME = 'a'
TAGS_CLASS_NAME = 'row playerList'
# Constants end

# create a phantom js driver
driver = CreatePhantomjsDriver(PHANTOMJS_PATH)

# Data Structure to store player name and detail link of each player


class Player:
    def __init__(self):
        self.name = ""
        self.link = ""


# download the html of that url
driver.get(URL)

# print(driver.page_source)  ## For debugging purpose

# create a soup object
soup = BeautifulSoup(driver.page_source, PARSER_NAME)

div = soup.find(ALL_PLAYERS_TAG_NAME, class_=ALL_PLAYERS_TAGS__CLASS_NAME)

# print(div)  # For debugging purpose

tag_list = div.find_all(TAG_NAME, class_=TAGS_CLASS_NAME)

player_list = []

for each_a_tag in tag_list:
    name, link = get_nba_player_name_and_detail_link(each_a_tag)

    new_player = Player()
    new_player.name = name
    new_player.link = link

    player_list.append(new_player)


get_nba_player_images(driver, player_list)

driver.quit()
