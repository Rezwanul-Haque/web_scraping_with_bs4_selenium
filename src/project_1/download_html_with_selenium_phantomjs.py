from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'F:\Rezwan\Work\Web Scraping\software\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)
