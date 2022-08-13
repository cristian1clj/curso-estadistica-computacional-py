from math import sqrt

class Coordiante:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def move(self, delta_x: int, delta_y: int):
        return Coordiante(delta_x + self.x, delta_y + self.y)
    
    def distance(self, another_coordinate) -> float:
        delta_x: int = self.x - another_coordinate.x
        delta_y: int = self.y - another_coordinate.y
        
        return sqrt(delta_x**2 + delta_y**2)