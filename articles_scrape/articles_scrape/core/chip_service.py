from typing import Any
from re import sub
from .base_parser import BaseParser


class ChipService(BaseParser):
    def get_title(self, response: Any) -> str:
        return response.css("h1::text").get(default="").strip()

    def get_category(self, response: Any) -> str:
        return response.css("div.fc-CategoryBadgeList a::text").get(default="").strip()

    def get_publication_date(self, response: Any) -> str:
        date = (
            response.css("span.text-neutral-700.dark\\:text-neutral-300::text")
            .get(default="")
            .split()
        )
        if not date:
            return (
                response.css('time[itemprop="datePublished"]::text')
                .get(default="")
                .strip()
            )
        return " ".join(date)

    def get_clean_content(self, response: Any) -> str:
        content_div = response.css("div#single-entry-content")
        if content_div:
            allowed_tags = ["h2", "h3", "p", "strong"]
            content = content_div.get()
            return sub(
                r"<(?!/?(:" + "|".join(allowed_tags) + r")\b)[^>]+>", "", content
            ).strip()
        return ""
