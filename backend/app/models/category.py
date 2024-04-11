from pydantic import BaseModel

from app.models.common import Category, Embedding, Probability


class CategoryPrediction(BaseModel):
    category: Category
    probability: Probability


class CategoryInput(BaseModel):
    category: Category
    embedding: Embedding
