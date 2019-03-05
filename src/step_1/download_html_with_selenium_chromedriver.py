from selenium import webdriver

driver = webdriver.Chrome(executable_path = r'E:\Razib\Workplace\Projects\Web Scraping\web_scraping_with_bs4_selenium\software\chromedriver_win32\chromedriver.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)
