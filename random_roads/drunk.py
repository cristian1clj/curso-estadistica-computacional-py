from random import choice
from typing import Tuple


class Drunk:
    def __init__(self, name: str) -> None:
        self.name = name


class TraditionalDrunk(Drunk):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def walk(self) -> Tuple[int, int]:
        return choice([(1, 0), (-1, 0), (0, -1), (0, 1)])