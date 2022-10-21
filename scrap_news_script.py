from lib2to3.pgen2 import driver
from unicodedata import category
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

my_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
my_driver.get("https://punchng.com/")

# Get webpage and parse
content = my_driver.page_source
soup = BeautifulSoup(content, features='html.parser')

# Data structure to store scraped  data
data = {
    'news-titles': [],
    'news-categories': [],
    'news-links': [],

}

# Find html element containing required data and store.
for div in soup.find_all('div', attrs={'class': 'post-content'}):
    news_title = div.find('h2', attrs={'class': 'post-title'})
    news_category = div.find('span', attrs={'class': 'post-category'})
    data['news-titles'].append(news_title.contents[0].string)
    data['news-links'].append(news_title.contents[0].get('href'))
    # data['news-categories'].append(news_category.contents[0].string)

print(data)
