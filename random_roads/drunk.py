from random import choice


class Drunk:
    def __init__(self, name: str) -> None:
        self.name = name


class TraditionalDrunk(Drunk):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def walk():
        return choice([(1, 0), (-1, 0), (0, -1), (0, 1)])