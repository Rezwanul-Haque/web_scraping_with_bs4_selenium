from .name import get_nba_player_name_and_detail_link

import os
import requests
import time
from bs4 import BeautifulSoup

def get_nba_player_images(driver, player_list:list, parser_name='lxml'):

    if not os.path.exists('media/img'):
        os.makedirs('media/img')

    for player in player_list:
        url = player.link

        driver.get(url)

        # print(driver.page_source)  ## For debugging purpose

        time.sleep(2)
        
        # # create a soup object
        soup = BeautifulSoup(driver.page_source, parser_name)

        div = soup.find("section", class_='nba-player-header__item nba-player-header__headshot')

        # # print(div)  # For debugging purpose

        img = div.find('img')

        pre_url = 'https:'

        img_link = pre_url + img['src']

        with open('media/img/{0}.jpg'.format(player.name), 'wb') as f:
            f.write(requests.get(img_link).content)
