from selenium import webdriver

driver = webdriver.Chrome(executable_path = r'F:\Rezwan\Work\Web Scraping\software\chromedriver.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)
