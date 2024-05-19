"""
The Coordinate class represents a geographical coordinate on the Earth's surface. 

It is initialized with two parameters: latitude and longitude, which are stored as instance variables. 

Instances of this class can be in distance calculations.
"""

class Coordinate:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude