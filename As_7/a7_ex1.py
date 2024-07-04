# K11720457
# Aral Cimcim

# Create a class Radian that converts degree angles.
class Radian:
    def __init__(self, degree: float):
        self.degree = degree
    
    def rad(self) -> float:
        return round(self.degree * (3.14 / 180.0), 2)
    
    def print(self):
        print(f"The degree is {self.degree:.2f} and the radian is {self.rad()}")

