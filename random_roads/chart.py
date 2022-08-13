from typing import Tuple

class Chart:
    def __init__(self) -> None:
        self.coordinates = {}
    
    def add_drunk(self, drunk, coordinate):
        self.coordinates[drunk] = coordinate
    
    def move_drunk(self, drunk):
        delta_x, delta_y = drunk.walk
        current_coordinate = self.coordinates[drunk]
        new_coordinate = current_coordinate.move(delta_x, delta_y)
        
        self.coordinates[drunk] = new_coordinate
    
    def consult_coordinate(self, drunk) -> Tuple[int, int]:
        return self.coordinates[drunk]