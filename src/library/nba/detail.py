def get_detail_for_all_player(player_list:list)->list:

    for player in player_list[0:2]:
        # if anyone want to overwrite url then un-comment it here and change it
        URL = player.link

        # download the html of that url
        driver.get(URL)

        # create a soup object
        soup = BeautifulSoup(driver.page_source, PARSER_NAME)

        Born = ""

        b_span = soup.find('span', string="BORN")

        for span in b_span.findNextSiblings():
            Born += span.text
        
        player.born = Born

    return player_list
