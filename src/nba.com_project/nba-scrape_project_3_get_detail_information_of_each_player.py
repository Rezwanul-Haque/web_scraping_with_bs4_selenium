import sys
sys.path.append("..")


from library.nba.name import get_nba_player_name, get_nba_player_name_and_detail_link, TAG_NAME, TAGS_CLASS_NAME
from library.nba.detail import get_detail_for_all_player
from library.drivers import CreatePhantomjsDriver
from settings.base import PHANTOMJS_PATH, URL

from bs4 import BeautifulSoup

# Height:
# Weight:
# Born:

# Constants
PARSER_NAME = 'lxml'  # Very fast, Lenient ## Their are other parsers available
# row players-wrapper  ## class name which contain all the player names
ALL_PLAYERS_TAG_NAME = 'div'
ALL_PLAYERS_TAGS__CLASS_NAME = 'row players-wrapper'
TAG_NAME = 'a'
TAGS_CLASS_NAME = 'row playerList'
# Constants end


class Player:
    def __init__(self):
        self.name = ""
        self.link = ""
        self.born = ""

# create a phantom js driver
driver = CreatePhantomjsDriver(PHANTOMJS_PATH)

# # if anyone want to overwrite url then un-comment it here and change it
# URL = "https://www.nba.com/players/bam/adebayo/1628389"

# # download the html of that url
# driver.get(URL)

# # create a soup object
# soup = BeautifulSoup(driver.page_source, PARSER_NAME)

# Height = ""
# h_span = children.findNextSiblings('p', string='HEIGHT', recursive=False)

# # print(h_span)
# for span in h_span.findNextSiblings():
#     Height += span.text

# Weight = ""
# w_span = soup.find('p', text="WEIGHT")

# # print(w_span)
# for span in w_span.findNextSiblings():
#     Weight += span.text

# Born = ""
# b_span = soup.find('span', string="BORN")

# for span in b_span.findNextSiblings():
#     Born += span.text

# create a soup object
soup = BeautifulSoup(driver.page_source, PARSER_NAME)

div = soup.find(ALL_PLAYERS_TAG_NAME, class_=ALL_PLAYERS_TAGS__CLASS_NAME)

tag_list = div.find_all(TAG_NAME, class_=TAGS_CLASS_NAME)

player_list = []

for each_a_tag in tag_list:
    name, link = get_nba_player_name_and_detail_link(each_a_tag)

    new_player = Player()
    new_player.name = name
    new_player.link = link

    player_list.append(new_player)

player_list = get_detail_for_all_player(player_list)

if __name__ == "__main__":
    # print(Height)
    # print(Weight)
    # print(Born)
    for player in player_list[0:2]:
        print(player_list.name)
        print(player_list.link)
        print(player_list.born)



