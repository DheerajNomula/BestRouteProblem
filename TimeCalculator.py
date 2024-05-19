"""
This class calculates the time taken to travel from source to destination at a given speed.
Using Strategy Pattern since it has-A relationship, in this case, the distance_calculator is the strategy, which can be any class that implements a calculate method.

Here's a brief explanation of how the Strategy Pattern is used:

TimeCalculator is the context. It uses a distance_calculator to calculate the travel time.
The distance_calculator is the strategy. It's an object that TimeCalculator uses to perform a calculation. The specific algorithm used for the calculation is determined by the class of distance_calculator.
HaversineCalculator is a concrete strategy. It's a specific implementation of the calculate method.

This design allows you to easily switch between different distance calculation algorithms. 
You can create new classes that implement the calculate method to add new algorithms.

"""

class TimeCalculator:
    def __init__(self, distance_calculator):
        self.distance_calculator = distance_calculator

    def travel_time(self, source, destination, speed):
        return self.distance_calculator.calculate(source, destination)/ speed