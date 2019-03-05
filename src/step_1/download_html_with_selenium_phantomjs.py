from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'E:\Razib\Workplace\Projects\Web Scraping\web_scraping_with_bs4_selenium\software\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)
