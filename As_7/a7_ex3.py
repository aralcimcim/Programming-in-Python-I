# K11720457
# Aral Cimcim

class Distance:
    def __init__(self, x: int):
        self.x = x
    
    def to_string(self) -> str:
        return f"{type(self).__name__}: the number of vectors ={self.x}"
    
    def dist(self) -> float:
        raise NotImplementedError("Distance must be implemented by all concrete subclasses")

