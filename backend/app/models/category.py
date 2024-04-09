from pydantic import BaseModel

from app.models.common import Probability, Category


class CategoryPrediction(BaseModel):
    category: Category
    probability: Probability
