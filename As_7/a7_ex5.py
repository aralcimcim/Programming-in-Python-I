# K11720457
# Aral Cimcim

from a7_ex3 import Distance

class Manhattan(Distance):
    def __init__(self, x:int, vect1: list, vect2: list):
        super().__init__(x)
        self.vect1 = vect1
        self.vect2 = vect2
    
    def to_string(self) -> str:
        return f"Manhattan: the number of vectors ={self.x}, vector_1={self.vect1}, vector_2={self.vect2}"
    
    def dist(self) -> float:
        manh_dist = sum(abs(x-y) for x,y in zip(self.vect1, self.vect2))
        return f"{manh_dist:.4f}"
    
