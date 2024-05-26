# Урок 7. Selenium в Python
import time
import csv
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 "
              "Safari/537.36")

chrome_options = Options()
chrome_options.add_argument(f'user_agent={user_agent}')

# Инициализация веб-драйвера
driver = webdriver.Chrome(options=chrome_options)

data = []

try:
    # Открытие сайта
    driver.get("https://books.toscrape.com")

    pause_time = 5
    # Переход в раздел Travel
    travel_link = driver.find_element(By.XPATH, '//ul/li/ul/li[1]/a')
    time.sleep(pause_time)
    travel_link.click()

    # Выполнение скроллинга страницы вниз
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
    time.sleep(pause_time)

    # Получение данных для сохранения
    book_titles = driver.find_elements(By.XPATH, '//h3/a')
    for title in book_titles:
        data.append(title.text)

    # Переход назад на главную страницу
    driver.back()
    time.sleep(pause_time)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()

    # Сохранение данных в CSV
    with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title'])
        writer.writerows(data)

    # Сохранение данных в JSON
    with open('books.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
