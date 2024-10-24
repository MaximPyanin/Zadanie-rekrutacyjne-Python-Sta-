BOT_NAME = "articles-scraper"

SPIDER_MODULES = ["articles-scraper.spiders"]
NEWSPIDER_MODULE = "articles-scraper.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Request fingerprinter implementation
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'  # Замените на желаемое значение

# Custom downloader middleware for Selenium
DOWNLOADER_MIDDLEWARES = {
    'articles-scraper.middlewares.ArticlesScraperDownloaderMiddleware': 543,
}

TELNETCONSOLE_ENABLED = False

# Settings for exporting data
FEEDS = {
    'response.json': {
        'format': 'json',
        'encoding': 'utf8',
        'indent': 4,
        'fields': ['title', 'category', 'publication_date', 'content'],  # fields to include in the output
        'overwrite': True,  # overwrite the output file each time
    }
}

# Log level (optional)
LOG_LEVEL = 'INFO'
