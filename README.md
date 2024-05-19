# BestRouteProblem

This repository contains the implementation of various routing algorithms that finds the best route for a delivery boy Aman. 

Assumptions made:
 starting node : Node with "Aman" 
 All the restaurant's are starting with R i.e. R1, R2, ... and all the customers are C1, C2, ... etc

## Files
distance_formulas directory contains different Distance calculators which can plugged/added based on the requirement

routing_algos contains different implementations to solve the existing problem

Two major implementation
1. Brute force by generating all permutations and then calculating the minimum distance
2. Using Travelling sales men appraoch to solve the given problem

TimeCalculator.py is the class that calculates the time take from a node to another based on the distance formula chosen.

Coordinates is the class that contains longitude and latitude. Instances of this class can be in distance calculations.

Helper.py has the utility methods that can be used in any of the classes
