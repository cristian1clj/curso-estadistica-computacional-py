from typing import Tuple
from coordiante import Coordiante

class Chart:
    def __init__(self) -> None:
        self.coordinates = {}
    
    def add_drunk(self, drunk, coordinate):
        self.coordinates[drunk] = Coordiante(coordinate[0], coordinate[1])
    
    def move_drunk(self, drunk):
        delta_x, delta_y = drunk.walk()
        
        current_coordinate = self.coordinates[drunk]
        new_coordinate = current_coordinate.move(delta_x, delta_y)
        
        self.coordinates[drunk] = Coordiante(new_coordinate[0], new_coordinate[1])
    
    def consult_coordinate(self, drunk) -> Tuple[int, int]:
        coordinate = self.coordinates[drunk]
        return coordinate.point()