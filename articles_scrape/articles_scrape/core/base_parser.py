from abc import ABC, abstractmethod
from typing import Any


class BaseParser(ABC):
    @abstractmethod
    def get_title(self, response: Any) -> str:
        pass

    @abstractmethod
    def get_category(self, response: Any) -> str:
        pass

    @abstractmethod
    def get_clean_content(self, response: Any) -> str:
        pass

    @abstractmethod
    def get_publication_date(self, response: Any) -> str:
        pass
