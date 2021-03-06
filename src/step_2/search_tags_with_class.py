from bs4 import BeautifulSoup

html_doc = """
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>The Dormouse's story</title>
      </head>
      <body>
          <p class="title">
            <b>The Dormouse's story</b>
          </p>
          <p class="story">Once upon a time there were three little sisters; and the.
          <a href="http://example.com/elsie" class="sister" id='link1'>Elsie</a>,
          <a href="http://example.com/lacie" class="sister" id='link2'>Lacie</a> and
          <a href="http://example.com/tillie" class="sister" id='link3'>Tillie</a>;
          and they lived at the bottom of a well.</p>
          <p class="story">...</p>
      </body>
    </html>
    """

soup = BeautifulSoup(html_doc, 'lxml')

p_tag = soup.find('p', class_='story')
print(p_tag)


p_tags = soup.findAll('p', class_='story')

print()
print(p_tags)
