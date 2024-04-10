from abc import ABC, abstractmethod
from typing import Awaitable

from app.models.latlon import LatLon


class RouteOptimizer(ABC):
    @abstractmethod
    def get_route(
        self,
        points: list[LatLon]
    ) -> Awaitable[list[LatLon] | None]:
        """
        Returns optimal route under 3h as subset from the given points
        order of given points does not matter, but the order of the resulting points matters
        and describes the exact path to follow or None if no such path is found
        """
        return NotImplemented
