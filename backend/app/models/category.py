from pydantic import BaseModel

from app.models.common import Category, Probability


class CategoryPrediction(BaseModel):
    category: Category
    probability: Probability
