import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = "https://www.divan.ru/category/divany-i-kresla"

driver.get(url)

time.sleep(3)

divans = driver.find_elements(By.CLASS_NAME, "lsooF")

parsed_data = []

for divan in divans:
    try:
        name = divan.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        link = divan.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
    except:
        print(f'Произошла ошибка при парсинге')
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("diva.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)