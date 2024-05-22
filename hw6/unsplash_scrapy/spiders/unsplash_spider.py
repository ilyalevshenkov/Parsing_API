import scrapy
import os
import requests
from PIL import Image
from io import BytesIO
import csv

class UnsplashSpider(scrapy.Spider):
    name = "unsplash"
    allowed_domains = ["unsplash.com"]
    start_urls = [
        'https://unsplash.com/t/travel'
    ]

    def parse(self, response):
        # Извлечение ссылок на изображения
        image_urls = response.css('img[srcset]').xpath('@src').getall()
        image_urls = [url.split('?')[0] for url in image_urls if url.startswith('https://images.unsplash.com/')]

        # Проверяем, чтобы папка существовала
        if not os.path.exists('images/travel'):
            os.makedirs('images/travel')

        # Открываем файл CSV для записи
        with open('images_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Image_URL', 'Local_Path', 'Title', 'Category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for idx, image_url in enumerate(image_urls[:10]):
                local_path = f'images/travel/image_{idx + 1}.jpg'
                self.download_image(image_url, local_path)

                # Получаем название и категорию изображения
                title = response.css('h1[itemprop="headline"]').xpath('text()').get()
                category = 'Travel'

                # Записываем информацию об изображении в CSV-файл
                writer.writerow({'Image_URL': image_url, 'Local_Path': local_path, 'Title': title, 'Category': category})

    def download_image(self, url, path):
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img.save(path)
            self.log(f'Successfully downloaded {url} to {path}')
        except Exception as e:
            self.log(f'Failed to download {url}. Error: {str(e)}')
