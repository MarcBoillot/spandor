import dataclasses


@dataclasses.dataclass
class Stock:
    red: int
    green: int
    blue: int
    black: int
    white: int

    def decrease(self, color, quantity):
        self.__dict__[color] -= quantity

    def increase(self, color, quantity):
        self.__dict__[color] += quantity


@dataclasses.dataclass
class Player:
    stock: Stock


# todo : renommer Board en Game
@dataclasses.dataclass
class Board:
    number_of_nobles: int
    stock: Stock
    yellow: int
    card_level_3: int
    card_level_2: int
    card_level_1: int
    players: list[Player]

