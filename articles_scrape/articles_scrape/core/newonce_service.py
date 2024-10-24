from typing import Any
from re import sub
from .base_parser import BaseParser


class NewonceService(BaseParser):
    def get_title(self, response: Any) -> str:
        return response.css("h1::text").get(default="").strip()

    def get_category(self, response: Any) -> list[str]:
        return response.css(
            "div.TagGroup_tags__7xpg3 a.TagGroup_tag__GM94X span.Tag_tag__MMKfG::text"
        ).getall()

    def get_publication_date(self, response: Any) -> str:
        return response.css(
            "time.Typography_visually-small__0s_jj.Article_date__yC9FI::text"
        ).get(default="")

    def get_clean_content(self, response: Any) -> str:
        content_div = response.css("div.Article_content__AZqFT")
        if content_div:
            allowed_tags = ["h2", "h3", "p", "strong", "em"]
            content = content_div.get()
            return sub(
                r"<(?!/?(:" + "|".join(allowed_tags) + r")\b)[^>]+>", "", content
            ).strip()
        return ""
