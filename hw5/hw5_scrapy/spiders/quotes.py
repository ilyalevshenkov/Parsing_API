import scrapy
import json
import csv

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()

            # Создаем словарь
            item = {
                'text': text,
                'author': author,
                'tags': ','.join(tags),
            }

            # JSON
            with open("quotes.json", "a", encoding="utf-8") as json_file:
                json.dump(item, json_file, ensure_ascii=False)
                json_file.write("\n")

            # CSV
            with open("quotes.csv", "a", newline="", encoding="utf-8") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=["text", "author", "tags"])
                if csv_file.tell() == 0:
                    writer.writeheader()
                writer.writerow(item)

        self.log("Цитаты сохранены в quotes.json и quotes.csv")

