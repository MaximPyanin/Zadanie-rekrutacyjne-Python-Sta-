from scrapy import Field, Item


class ArticlesScraperItem(Item):
    title = Field()
    category = Field()
    publication_date = Field()
    content = Field()
