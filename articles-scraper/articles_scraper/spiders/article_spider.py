from re import sub
from typing import Any

from scrapy import Request
from scrapy import Spider

from articles_scraper.items import ArticlesScraperItem
from articles_scraper.services.config_service import AppConfig
class ArticleSpider(Spider):
    name = 'article_spider'
    def __init__(self, config: AppConfig, **kwargs: Any):
        super().__init__(**kwargs)
        self.config = config

    def start_requests(self):
        yield Request(url=self.config.BASE_URL + self.config.ARTICLE_ONE, callback=self.parse)
        yield Request(url=self.config.BASE_URL + self.config.ARTICLE_TWO, callback=self.parse)


    def parse(self, response):
        # Извлечение данных
        item = ArticlesScraperItem()
        item['title'] = response.css('h1::text').get(default='').strip()

        # Извлечение категории из первого тега <a> вверху страницы
        # Find <a> elements with category-related keywords in the href attribute
        item['category'] = response.css(
    'a[href*="kategoria"]::text, a[href*="kategorie"]::text, a[href*="tag"]::text, '
    'a[href*="temat"]::text, a[href*="kategoria"] span::text, '
    'a[href*="kategoria"] div::text'
).getall()

        item['publication_date'] = response.css(
    'time[datetime]::attr(datetime), span::text, div::text'
).re_first(r'\d{2}\.\d{2}\.\d{4}|\d{2}\s\w+\s\d{4}|\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}')
        item['content'] = self.clean_content(response)

        yield item

    def clean_content(self, response):
        # Находим все <div>, где в классе есть слово "content"
        divs = response.css('div[class*="content"]').getall()

        # Выбираем самый большой <div> по количеству текста
        largest_div = max(divs, key=lambda div: len(sub(r'<[^>]+>', '', div)))

        # Оставляем только разрешенные теги
        allowed_tags = ['h2', 'h3', 'p', 'strong']
        cleaned_html = sub(r"<(?!/?(?:" + '|'.join(allowed_tags) + r")\b)[^>]+>", '', largest_div)

        # Логирование для отладки
        self.logger.info(f"Cleaned Content: {cleaned_html}")

        return cleaned_html.strip()
