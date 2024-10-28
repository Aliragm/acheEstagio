from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Safari()
driver.get("https://www.estagiotrainee.com/blog/categories/estágio")


def scroll_down(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

scroll_down(driver)

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

oportunities = soup.find_all('a', {'class':'O16KGI pu51Xe x_FPRX xs2MeC'})

title, link = [], []
for oportunity in oportunities:
    title.append(oportunity.text)
    link.append(oportunity['href'])

data = pd.DataFrame({'Titulo': title, 'Link': link})
data.to_html('teste.html')