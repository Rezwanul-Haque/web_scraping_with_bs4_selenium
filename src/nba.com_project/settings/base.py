import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

PHANTOMJS_PATH = BASE_DIR + \
    '/software/Ubuntu/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'

# web page url which should be scrape
URL = 'https://www.nba.com/players'
