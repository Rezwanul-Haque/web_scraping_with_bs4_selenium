import sys
import requests
sys.path.append("..")

from library.nba.name import get_nba_player_name_and_detail_link, TAG_NAME, TAGS_CLASS_NAME
from library.drivers import CreatePhantomjsDriver
from settings.base import PHANTOMJS_PATH, URL
from bs4 import BeautifulSoup


# Constants
# if anyone want to overwrite url then un-comment it here and change it
URL = "https://www.nba.com/players/bam/adebayo/1628389"
PARSER_NAME = 'lxml'  # Very fast, Lenient ## Their are other parsers available
# row players-wrapper  ## class name which contain all the player names
ALL_PLAYERS_TAG_NAME = 'div'
ALL_PLAYERS_TAGS__CLASS_NAME = 'row players-wrapper'
TAG_NAME = 'a'
TAGS_CLASS_NAME = 'row playerList'
# Constants end

# create a phantom js driver
driver = CreatePhantomjsDriver(PHANTOMJS_PATH)

# Data Structure to store player name and detail link of each player
# class Player:
#     def __init__(self):
#         self.name = ""
#         self.link = ""


# # download the html of that url
driver.get(URL)

# print(driver.page_source)  ## For debugging purpose

# # create a soup object
soup = BeautifulSoup(driver.page_source, PARSER_NAME)

div = soup.find("section", class_='nba-player-header__item nba-player-header__headshot')

# # print(div)  # For debugging purpose

img = div.find('img')

pre_url = 'https:'

img_link = pre_url + img['src']

with open('media/bam.jpg', 'wb') as f:
    f.write(requests.get(img_link).content)


driver.quit()

# tag_list = div.find_all(TAG_NAME, class_=TAGS_CLASS_NAME)

# player_list = []

# for each_a_tag in tag_list:
#     name, link = get_nba_player_name_and_detail_link(each_a_tag)
