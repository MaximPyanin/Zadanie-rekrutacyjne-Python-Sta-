import os
from dotenv import load_dotenv
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from articles_scrape import settings as project_settings
from articles_scrape.services.config_service import AppConfig
from articles_scrape.spiders.articles_scrape import ArticleSpider


def main():
    config = AppConfig(os.environ)
    settings = Settings()
    settings.setmodule(project_settings)

    process = CrawlerProcess(settings)
    process.crawl(ArticleSpider, config=config)
    process.start()


if __name__ == "__main__":
    load_dotenv()
    main()
