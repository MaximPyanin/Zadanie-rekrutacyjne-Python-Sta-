from scrapy import Field


class ArticlesScraperItem(scrapy.Item):
    title = Field()
    category = Field()
    publication_date = Field()
    content = Field()
