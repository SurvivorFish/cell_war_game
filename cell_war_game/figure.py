import alphabet
from dataclasses import dataclass, field


@dataclass
# Not sure, do I need this class. I'm using it to remember, what should I add to other figure classes.
# And, maybe it's good for board.py.
class Figure:
    name: str
    place: alphabet.Place
    moves: list[tuple[int, int]]
    # moves:list[tuple[int, int]] = field(default_factory=list)
    # Don't know how to use it. This line shows an error...
    team: alphabet.Team

    def __init__(self, name: str, place: alphabet.Place, moves: list[tuple[int, int]], team: alphabet.Team):
        self.name = name
        self.place = place
        self.moves = moves
        self.team = team
        self.pos_moves = [self.place+move for move in self.moves]  # possible moves


class Guy(Figure):
    moves = [(-1, -1), (0, -1), (1, -1),
             (-1, 0), (1, 0),
             (-1, 1), (0, 1), (1, 1)]

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(Guy, self).__init__('guy', alphabet.Place(x, y), self.moves, team)


class Cat(Figure):
    moves = [(-1, -1), (0, -1), (1, -1),
             (-1, 0), (1, 0),
             (-1, 1), (0, 1), (1, 1)]

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(Cat, self).__init__('cat', alphabet.Place(x, y), self.moves, team)


class King(Figure):
    moves = [(-1, -1), (0, -1), (1, -1),
             (-1, 0), (1, 0),
             (-1, 1), (0, 1), (1, 1)]

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(King, self).__init__(team.name, alphabet.Place(x, y), self.moves, team)
