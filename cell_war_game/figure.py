import BM
from dataclasses import dataclass


@dataclass
class Figure:
    name: str
    place: BM.Place
    moves: []
    team: str


class Guy(Figure):
    moves = [(-1, -1), (0, -1), (1, -1)]

    def __init__(self, x, y, team):
        self.name = 'guy'
        self.place = BM.Place(x, y)
        self.team = team


class Cat(Figure):
    def __init__(self, x, y, team):
        self.name = 'cat'
        self.place = BM.Place(x, y)
        self.team = team


class King(Figure):
    def __init__(self, x, y, team):
        self.name = team.name
        self.place = BM.Place(x, y)
        self.team = team
