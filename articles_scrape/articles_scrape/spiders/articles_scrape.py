from typing import Any, Generator
from scrapy import Request, Spider
from ..items import ArticlesScraperItem
from ..constants.urls import URLS
from ..services.config_service import AppConfig


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

        for url_enum in URLS:
            if response.url.startswith(url_enum.domain):
                service = url_enum.service
                item["title"] = service.get_title(response)
                item["category"] = service.get_category(response)
                item["publication_date"] = service.get_publication_date(response)
                item["content"] = service.get_clean_content(response)
                break

        yield item
