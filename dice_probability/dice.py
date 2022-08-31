from random import choice


class Dice:
    def __init__(self, num_sides: int) -> None:
        self.num_sides = num_sides
    
    def result(self) -> int:
        return choice(range(1, self.num_sides + 1))