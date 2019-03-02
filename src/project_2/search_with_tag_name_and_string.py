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
          <a href="http://example.com/tillie" class="sister" id='link3' name='tillie'>Tillie</a>;
          and they lived at the bottom of a well.</p>
          <p class="story">...</p>
      </body>
    </html>
    """

soup = BeautifulSoup(html_doc, 'lxml')

a_lacie = soup.findAll('a', string= 'Lacie') ## Search by strings of html tags

print(a_lacie)
