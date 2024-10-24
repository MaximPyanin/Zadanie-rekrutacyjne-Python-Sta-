from re import sub
from typing import Any, Generator
from scrapy import Request, Spider
from articles_scraper.items import ArticlesScraperItem
from articles_scraper.services.config_service import AppConfig


class ArticleSpider(Spider):
    name = "article_spider"

    def __init__(self, config: AppConfig, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.config = config

    def start_requests(self) -> Generator[Request, None, None]:
        for article in [self.config.ARTICLE_ONE, self.config.ARTICLE_TWO]:
            yield Request(url=f"{self.config.BASE_URL}{article}", callback=self.parse)

    def parse(self, response: Any) -> ArticlesScraperItem:
        item = ArticlesScraperItem()
        item["title"] = response.css("h1::text").get(default="").strip()
        item["category"] = response.css(
            'a[href*="kategoria"]::text, a[href*="kategorie"]::text, '
            'a[href*="tag"]::text, a[href*="temat"]::text, '
            'a[href*="kategoria"] span::text, a[href*="kategoria"] div::text'
        ).getall()
        item["publication_date"] = response.css(
            "time[datetime]::attr(datetime), span::text, div::text"
        ).re_first(
            r"\d{2}\.\d{2}\.\d{4}|\d{2}\s\w+\s\d{4}|\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}"
        )
        item["content"] = self.extract_clean_content(response)

        yield item

    def extract_clean_content(self, response: Any) -> str:
        divs = response.css('div[class*="content"]').getall()
        largest_div = max(divs, key=lambda div: len(sub(r"<[^>]+>", "", div)))
        allowed_tags = ["h2", "h3", "p", "strong"]
        cleaned_html = sub(
            r"<(?!/?(?:" + "|".join(allowed_tags) + r")\b)[^>]+>", "", largest_div
        )

        return cleaned_html.strip()
