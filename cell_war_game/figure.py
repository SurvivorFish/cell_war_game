import alphabet
from dataclasses import dataclass, field


@dataclass
# Not sure, do I need this class. I'm using it to remember, what should I add to other figure classes.
# And, maybe it's good for board.py.
class Figure:
    name: str
    place: alphabet.Place
    jump: bool   # Can jump over the other pieces
    swing: bool  # Can attack through another pieces
    move: list[tuple[int, int]]
    attack: list[tuple[int, int]]
    capture: list[tuple[int, int]]
    charge: list[tuple[int, int]]
    team: alphabet.Team

    def __init__(self, name: str, place: alphabet.Place,
                 move: list[tuple[int, int]], attack: list[tuple[int, int]], capture: list[tuple[int, int]],
                 charge: list[tuple[int, int]], team: alphabet.Team):
        self.name = name
        self.place = place
        self.move = move
        self.attack = attack
        self.capture = capture
        self.charge = charge
        self.team = team

    def goto(self, place):
        if isinstance(place, alphabet.Place): self.place = alphabet.Place(place.x, place.y)
        if isinstance(place, tuple): self.place = alphabet.Place(place[0], place[1])
        return place


class Guy(Figure):
    move = [(-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)]

    attack = move
    capture = move
    charge = []

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(Guy, self).__init__('guy', alphabet.Place(x, y), self.move, self.attack, self.capture, self.charge, team)


class Cat(Figure):  # Really strange piece
    move = [(-2, -2), (0, -2), (2, -2),
             (-2, 0), (2, 0),
             (-2, 2), (0, 2), (2, 2)]

    attack = move
    capture = move
    charge = move

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(Cat, self).__init__('cat', alphabet.Place(x, y), self.move, self.attack, self.capture, self.charge, team)


class King(Figure):
    move = [(-1, -1), (0, -1), (1, -1),
             (-1, 0), (1, 0),
             (-1, 1), (0, 1), (1, 1)]
    attack = move
    capture = move
    charge = []

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(King, self).__init__(team.name, alphabet.Place(x, y),
                                   self.move, self.attack, self.capture, self.charge, team)


class Pawn(Figure):  # Buffed pawn, I will change it in next updates, maybe
    move = [(-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)]

    attack = []
    capture = move
    charge = []

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(Pawn, self).__init__('pwn', alphabet.Place(x, y), self.move, self.attack, self.capture, self.charge, team)


class Knight(Figure):
    move = [(-1, -2), (1, -2),
            (-2, 1), (-2, -1), (2, 1), (2, -1),
            (-1, 2), (1, 2)]

    attack = []
    capture = move
    charge = []

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(Knight, self).__init__('knt', alphabet.Place(x, y),
                                     self.move, self.attack, self.capture, self.charge, team)


class Bishop(Figure):
    move = []

    for i in range(1, 9):
        move.append((i, i))
        move.append((i, -i))
        move.append((-i, i))
        move.append((-i, -i))

    attack = []
    capture = move
    charge = []

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(Bishop, self).__init__('bhp', alphabet.Place(x, y),
                                     self.move, self.attack, self.capture, self.charge, team)


class Rook(Figure):
    move = []

    for i in range(1, 9):
        move.append((0, i))
        move.append((0, -i))
        move.append((i, 0))
        move.append((-i, 0))


    attack = []
    capture = move
    charge = []

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(Rook, self).__init__('ruk', alphabet.Place(x, y), self.move, self.attack, self.capture, self.charge, team)


class Queen(Figure):
    move = []

    for i in range(1, 9):
        move.append((0, i))
        move.append((0, -i))
        move.append((i, 0))
        move.append((-i, 0))

        move.append((i, i))
        move.append((i, -i))
        move.append((-i, i))
        move.append((-i, -i))

    attack = []
    capture = move
    charge = []

    def __init__(self, x: int, y: int, team: alphabet.Team):
        super(Queen, self).__init__('QUE', alphabet.Place(x, y), self.move, self.attack, self.capture, self.charge, team)
