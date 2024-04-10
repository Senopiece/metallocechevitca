from typing import List
import math
from app.models.latlon import LatLon
from app.repos.route_optimizer import RouteOptimizer


class ManhettanRouteOptimizer(RouteOptimizer):
    # Manhettan router with some heuristics
    async def get_route(self, points: List[LatLon]) -> List[LatLon]:
        if not points:
            return []

        # Convert latitude and longitude to approximate kilometers to use for distance calculations
        points_in_km = [
            (point.lat * 111, point.lon * 111 * math.cos(math.radians(point.lat)))
            for point in points
        ]

        route = [points[0]]  # Starting from the first point in the list
        visited = set([0])
        total_distance = 0

        # Assuming the average walking speed is about 5 kilometers per hour (which is a commonly used estimate),
        # and given that there are 3 hours available,
        # the maximum distance that can be covered is 5 * 3 = 15 kilometers.
        while len(visited) < len(points) and total_distance <= 15:
            last_index = points.index(route[-1])
            last_point_in_km = points_in_km[last_index]
            nearest_point_index = None
            min_distance = float('inf')

            for i, point in enumerate(points_in_km):
                if i not in visited:
                    distance = abs(last_point_in_km[0] - point[0]) + abs(last_point_in_km[1] - point[1])
                    if distance < min_distance:
                        min_distance = distance
                        nearest_point_index = i

            if nearest_point_index is not None and (total_distance + min_distance <= 15):
                total_distance += min_distance
                visited.add(nearest_point_index)
                route.append(points[nearest_point_index])
            else:
                break  # No further points can be added without exceeding the distance limit

        return route
