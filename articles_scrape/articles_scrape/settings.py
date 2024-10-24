BOT_NAME = "articles_scrape"

SPIDER_MODULES = ["articles_scrape.spiders"]
NEWSPIDER_MODULE = "articles_scrape.spiders"

ROBOTSTXT_OBEY = True


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"


DOWNLOADER_MIDDLEWARES = {
    "articles_scrape.middlewares.ArticlesScraperMiddleware": 543,
}

TELNETCONSOLE_ENABLED = False


FEEDS = {
    "response.json": {
        "format": "json",
        "encoding": "utf8",
        "indent": 4,
        "fields": ["title", "category", "publication_date", "content"],
        "overwrite": True,
    }
}

LOG_LEVEL = "INFO"
