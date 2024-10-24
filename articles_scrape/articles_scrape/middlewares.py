from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.http import Request
from scrapy.spiders import Spider


class ArticlesScraperMiddleware:
    @classmethod
    def from_crawler(cls, crawler: Spider) -> "ArticlesScraperMiddleware":
        return cls()

    def __init__(self) -> None:
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.web_driver = webdriver.Chrome(service=service, options=chrome_options)

    def process_request(self, request: Request, spider: Spider) -> HtmlResponse:
        self.web_driver.get(request.url)
        page_body = self.web_driver.page_source
        return HtmlResponse(
            self.web_driver.current_url,
            body=page_body,
            encoding="utf-8",
            request=request,
        )

    def spider_closed(self, spider: Spider) -> None:
        self.web_driver.quit()
