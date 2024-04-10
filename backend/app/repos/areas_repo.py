from abc import ABC, abstractmethod

from app.models.area import Area


class AreasRepo(ABC):
    @abstractmethod
    def get_areas(self) -> list[Area]:
        return NotImplemented
