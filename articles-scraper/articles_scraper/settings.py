BOT_NAME = "articles-scraper"

SPIDER_MODULES = ["articles-scraper.spiders"]
NEWSPIDER_MODULE = "articles-scraper.spiders"

ROBOTSTXT_OBEY = True


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"


DOWNLOADER_MIDDLEWARES = {
    "articles-scraper.middlewares.ArticlesScraperDownloaderMiddleware": 543,
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
