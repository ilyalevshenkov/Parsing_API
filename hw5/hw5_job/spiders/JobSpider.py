import scrapy
from scrapy.http import HtmlResponse

class JobSpider(scrapy.Spider):
    name = "JobSpider"
    allowed_domains = ["hh.ru"]
    start_urls = [
        "https://hh.ru/search/vacancy?from=suggest_post&hhtmFrom=main&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&text=Python&enable_snippets=false&L_save_area=true"
    ]

    def parse(self, response: HtmlResponse):
        # Проверяем наличие следующей страницы и переходим на нее
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        # Получаем ссылки на вакансии и переходим по каждой из них
        links = response.xpath("//a[@data-qa='vacancy-serp__vacancy-title']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        # Извлекаем данные о вакансии
        name = response.xpath("//h1/text()").get()
        salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        salary = ''.join(salary).strip()  # Преобразуем список текста в одну строку
        url = response.url
        url_base = url.split("?")[0]
        _id = url_base.split("/")[-1]

        # Возвращаем собранные данные
        yield {
            "id": _id,
            "name": name,
            "salary": salary,
            "url": url
        }
