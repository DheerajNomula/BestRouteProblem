import math

from DistanceCalculator import DistanceCalculator

"""
Using inheritance,

HaversineCalculator is a subclass of DistanceCalculator that uses the Haversine formula to calculate the distance between two points on the Earth's surface, given their longitude and latitude.

The class overrides the `calculate` method of DistanceCalculator with its own `haversine` method. The `haversine` method takes two tuples as parameters, each representing the latitude and longitude of a point. It returns the distance between these points in kilometers.

The class is initialized with the `haversine` method as the formula for distance calculation. This is done in the `__init__` method, which calls the `__init__` method of DistanceCalculator with `haversine` as the parameter.

Resource Link: https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128#:~:text=For%20example%2C%20haversine(%CE%B8),longitude%20of%20the%20two%20points.

"""

class HaversineDistanceCalculator(DistanceCalculator):
    @staticmethod
    def haversine(source, destination):
        lat1, lon1 = source
        lat2, lon2 = destination
        radius = 6371  # for KM

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius * c

        return distance

    def __init__(self):
        super().__init__(self.haversine)