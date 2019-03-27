"""[This function will get the NBA player names]

Returns:
    [list] -- [player names will be return as a list]
"""


TAG_NAME = ""
TAGS_CLASS_NAME = ""

def get_nba_player_name(div_name: list, tag_name: str, class_name: str) -> list:
    """For getting the names of NBA player and return the names as a list
    
    Arguments:
        div_name {list} -- [The div that contain all the players name]
        tag_name {str} -- [The tag name which contain the name of the Player]
        class_name {str} -- [class name which identify the tag]
    """

    name_list = [tag.text for tag in div_name.find_all(tag_name, class_=class_name)]

    return name_list
