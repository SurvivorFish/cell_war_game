import BM
from dataclasses import dataclass


@dataclass
# Not sure, do I need this class. I'm using it to remember, what should I add to other figure classes.
# And, maybe it's good for board.py.
class Figure:
    name: str
    place: BM.Place
    moves: []
    team: BM.Team


class Guy(Figure):
    moves = [(-1, -1), (0, -1), (1, -1)]

    def __init__(self, x: int, y: int, team: BM.Team):
        self.name = 'guy'
        self.place = BM.Place(x, y)
        self.team = team


class Cat(Figure):
    def __init__(self, x: int, y: int, team: BM.Team):
        self.name = 'cat'
        self.place = BM.Place(x, y)
        self.team = team


class King(Figure):
    def __init__(self, x: int, y: int, team: BM.Team):
        self.name = team.name
        self.place = BM.Place(x, y)
        self.team = team
