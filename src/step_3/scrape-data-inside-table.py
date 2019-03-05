from bs4 import BeautifulSoup

soup = BeautifulSoup(open('sample.html'), 'lxml')

# print(soup.prettify())

for tr in soup.findAll('tr'):
    for td in tr.findAll('td'):
        print(td.text)
