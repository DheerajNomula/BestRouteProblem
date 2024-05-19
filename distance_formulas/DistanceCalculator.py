class DistanceCalculator:
    def __init__(self, formula):
        self.formula = formula

    def calculate(self, source, destination):
        return self.formula(source, destination)