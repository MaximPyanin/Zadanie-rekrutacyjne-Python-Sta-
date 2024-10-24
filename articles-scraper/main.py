import os
from dotenv import load_dotenv
from scrapy.crawler import CrawlerProcess
from articles_scraper.spiders.article_spider import ArticleSpider
from services.config_service import AppConfig
from scrapy.settings import Settings
from articles_scraper import settings as s
def main():
    config = AppConfig(os.environ)

    settings = Settings()
    settings.setmodule(s)

    process = CrawlerProcess(settings)
    spider = ArticleSpider(config=config)
    process.crawl(spider)
    process.start()

if __name__ == '__main__':
    load_dotenv()
    main()
