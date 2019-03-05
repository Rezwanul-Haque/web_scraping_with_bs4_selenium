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
          <div>
          <p class="story">Once upon a time there were three little sisters; and the.
              <a href="http://example.com/elsie" class="sister" id='link1'>Elsie</a>,
              <a href="http://example.com/lacie" class="sister" id='link2'>Lacie</a> and
              <a href="http://example.com/tillie" class="sister" id='link3' name='tillie'>Tillie</a>;
          and they lived at the bottom of a well.
          </p>
          <p class="story">...</p>
          </div>
      </body>
    </html>
    """

soup = BeautifulSoup(html_doc, 'lxml')

# # search for all child
# p = soup.find('p', class_='story')
# all_p_children = p.findChildren()
#
# print(all_p_children)

# # search for parent
# p = soup.find('p', class_='story')
# p_parent = p.findParent()
#
# print(p_parent)

# Search for sibling
first_a = soup.find('a')

remain_sibling = first_a.findNextSiblings()

print(remain_sibling)
