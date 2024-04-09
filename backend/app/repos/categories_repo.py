from abc import ABC, abstractmethod

from app.models.category import CategoryPrediction
from app.models.common import Embedding


class CategoriesRepo(ABC):
    @abstractmethod
    def get_most_similar_categories(
        self, embedding: Embedding
    ) -> list[CategoryPrediction]:
        return NotImplemented
