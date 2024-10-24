from typing import Any
from re import sub
from .base_parser import BaseParser


class SpidersWebService(BaseParser):
    def get_title(self, response: Any) -> str:
        return response.css("h1::text").get(default="").strip()

    def get_category(self, response: Any) -> str:
        return (
            response.css(
                'li[itemprop="itemListElement"] a[itemprop="item"][href*="kategoria"] span[itemprop="name"]::text'
            )
            .get(default="")
            .strip()
        )

    def get_publication_date(self, response: Any) -> str:
        date_spans = response.css('time[itemprop="datePublished"] span::text').getall()
        if date_spans:
            return " ".join(span.strip() for span in date_spans)
        return (
            response.css('time[itemprop="datePublished"]::text').get(default="").strip()
        )

    def get_clean_content(self, response: Any) -> str:
        content_div = response.css(
            "div.CompositionGridContentWithSidebar_content__AYfoV"
        )
        if content_div:
            allowed_tags = ["h2", "h3", "p", "strong"]
            content = content_div.get()
            return sub(
                r"<(?!/?(:" + "|".join(allowed_tags) + r")\b)[^>]+>", "", content
            ).strip()
        return ""
