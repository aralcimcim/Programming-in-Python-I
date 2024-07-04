import math

class Angle:
    def __init__(self, degree: float = None, radian: float = None):
        if degree == None and radian == None:
            raise ValueError("Either degree or radian must be specified.")
        
        self.degree = degree
        self.radian = radian

        if degree != None and radian != None:
            if self.consistency() == False:
                raise ValueError("Degree and radian are not consistent.")

        elif degree != None:
            self.radian = self.deg_to_rad(degree)

        elif radian != None:
            self.degree = self.rad_to_deg(radian)

    def consistency(self):
        return math.isclose(self.deg_to_rad(self.degree), self.radian) and math.isclose(self.rad_to_deg(self.radian), self.degree)

    def __eq__(self, other):
        if isinstance(other, Angle):
            return math.isclose(self.degree, other.degree) and math.isclose(self.radian, other.radian)
        
        else:
            return NotImplemented
        
    def __repr__(self):
        return f"Angle(degree={self.degree:.3f}, radian={self.radian:.3f})"

    def __str__(self):
        return f"{self.degree:.2f} deg = {self.radian:.2f} rad"

    def __add__(self, other):
        if isinstance(other, Angle):
            return Angle(self.degree + other.degree, self.radian + other.radian)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Angle):
            self.degree += other.degree
            self.radian += other.radian
            if self.consistency() == False:
                raise ValueError("Degree and radian are not consistent.")
            return self
        else:
            return NotImplemented

    @staticmethod
    def deg_to_rad(degree):
        return degree * (math.pi / 180)

    @staticmethod
    def rad_to_deg(radian):
        return radian * (180 / math.pi)

    @staticmethod
    def add_all(angle, *angles):
        sum_degrees = angle.degree
        sum_rads = angle.radian

        for angle in angles:
            sum_degrees += angle.degree
            sum_rads += angle.radian

        return Angle(sum_degrees, sum_rads)

