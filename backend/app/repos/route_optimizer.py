from abc import ABC, abstractmethod

from models.latlon import LatLon


class RouteOptimizer(ABC):
    @abstractmethod
    def get_route(
        self,
        points: list[LatLon]
    ) -> list[LatLon]:
        """
        Returns optimal route under 3h as subset from the given points
        order of given points does not matter, but the order of the resulting points matters
        and describes the exact path to follow
        """
        return NotImplemented