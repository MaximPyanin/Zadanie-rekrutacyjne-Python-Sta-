from typing import Any
from re import sub
from .base_parser import BaseParser


class BistrolubieService(BaseParser):
    def get_title(self, response: Any) -> str:
        return response.css("h1::text").get(default="").strip()

    def get_category(self, response: Any) -> str:
        return response.css("a.bg-red.uppercase-text::text").get(default="")

    def get_publication_date(self, response: Any) -> str:
        return (
            response.css("div.flex.items-center.gap-2.font-sans span::text")
            .get(default="")
            .strip()
        )

    def get_clean_content(self, response: Any) -> str:
        divs = response.css("div").getall()
        largest_div = max(divs, key=lambda div: len(sub(r"<[^>]+>", "", div)))
        allowed_tags = ["h2", "h3", "p", "strong"]
        return sub(
            r"<(?!/?(:" + "|".join(allowed_tags) + r")\b)[^>]+>", "", largest_div
        ).strip()
