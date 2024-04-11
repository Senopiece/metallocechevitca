from abc import ABC, abstractmethod

from app.models.category import CategoryInput, CategoryPrediction
from app.models.common import Embedding


class CategoriesRepo(ABC):
    @abstractmethod
    def get_most_similar_categories(
        self, embedding: Embedding
    ) -> list[CategoryPrediction]:
        return NotImplemented

    @abstractmethod
    def add_category(self, category: CategoryInput) -> bool:
        return NotImplemented
