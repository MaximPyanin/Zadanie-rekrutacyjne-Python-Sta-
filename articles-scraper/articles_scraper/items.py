import scrapy

class ArticlesScraperItem(scrapy.Item):
    title = scrapy.Field()  # Field for the article title
    category = scrapy.Field()  # Field for the article category
    publication_date = scrapy.Field()  # Field for the publication date
    content = scrapy.Field()  # Field for the article content
