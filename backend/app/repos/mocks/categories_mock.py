from app.models.category import CategoryPrediction
from app.models.common import Embedding
from app.repos.categories_repo import CategoriesRepo


class CategoriesMock(CategoriesRepo):
    def get_most_similar_categories(
        self, embedding: Embedding
    ) -> list[CategoryPrediction]:
        return [
            CategoryPrediction(category="памятник", probability=0.9),
            CategoryPrediction(category="музей", probability=0.7),
            CategoryPrediction(category="театр", probability=0.5),
        ]