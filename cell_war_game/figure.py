from dataclasses import dataclass
from enum import Enum

import alphabet
from board import Board


_ALL_DIRECTIONS = [
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def _direction(d: int):
    if d < len(_ALL_DIRECTIONS):
        return _ALL_DIRECTIONS[d]
    return None


# Enums
class MoveType(Enum):
    MOVE = "move"
    ATTACK = "attack"
    CAPTURE = "capture"
    CHARGE = "charge"


@dataclass
class Figure:
    '''
    Here you can place doc comments, for example:
    
    :param direct: Piece direction:
      - 321
      - 4*0
      - 567
      - * = -1 - special direction
    '''
    name: str
    place: alphabet.Place
    jump: int  # Type of jumping
    swing: int  # Type of "swinging" through figures
    move_len: int
    attack_len: int
    direct: int  
    moves: dict[MoveType, list[tuple[int, int]]]
    team: alphabet.Team

    def goto(self, place):
        if isinstance(place, alphabet.Place): self.place = alphabet.Place(place.x, place.y)
        if isinstance(place, tuple): self.place = alphabet.Place(place[0], place[1])
        return place
    
    def _reachable_places(self, move_type: MoveType, board: Board) -> list[list[int]]:
        ''' dfs or bfs '''
        pass

    def can(self, type_of_move: MoveType, boardik: Board):
        move_mas = self.moves.get(type_of_move, [])
        move_len = 8

        net = []
        walls = []
        for i in range(boardik.w):
            net_row = []
            walls_row = []
            for j in range(boardik.h):
                if boardik.names[i][j] != "   ":
                    walls_row.append(-1)
                else:
                    walls_row.append(0)
                net_row.append(0)
            net.append(net_row)
            walls.append(walls_row)
        net[self.place.x][self.place.y] = 1
        if ((type_of_move == 'move' or type_of_move == 'capture') and self.jump == 0) \
                or ((type_of_move == 'attack' or type_of_move == 'charge') and self.swing == 0):  # example
            for k in range(move_len):
                for i in range(boardik.w):
                    for j in range(boardik.h):
                        if walls[i][j] != -1:
                            Maxes = []
                            if i > 0 and net[i - 1][j] > 0:
                                Maxes.append(net[i - 1][j])
                            if j > 0 and net[i][j - 1] > 0:
                                Maxes.append(net[i][j - 1])
                            if i < boardik.w - 1 and net[i + 1][j] > 0:
                                Maxes.append(net[i + 1][j])
                            if j < boardik.h - 1 and net[i][j + 1] > 0:
                                Maxes.append(net[i][j + 1])
                            if len(Maxes) > 0:
                                net[i][j] = max(Maxes) + 1
                            else:
                                net[i][j] = 0
        elif ((type_of_move == 'move' or type_of_move == 'capture') and self.jump == 1) \
                or ((
                            type_of_move == 'attack' or type_of_move == 'charge') and self.swing == 1):  # Only on move places (8 neighbours)
            flag = True
            while flag:
                flag = False
                for move in move_mas:
                    i = (self.place + move).x
                    j = (self.place + move).y
                    if 0 <= j < boardik.h and 0 <= i < boardik.w:
                        if walls[i][j] == -1:
                            continue
                        if net[i][j] == 0:
                            flag = True
                        Maxes = []
                        
                        for dx, dy in _ALL_DIRECTIONS:
                            i2, j2 = i + dx, j + dy
                            if 0 <= i2 < boardik.width and 0 <= j2 < boardik.height:
                                Maxes.append(net[i2][j2])
                            
                        if len(Maxes) > 0:
                            net[i][j] = max(Maxes) + 1
                        else:
                            flag = False
                            net[i][j] = 0

            # Can jump over everything
        elif ((type_of_move == 'move' or type_of_move == 'capture') and self.jump == 2) \
                or ((type_of_move == 'attack' or type_of_move == 'charge') and self.swing == 2):
            for i in range(boardik.w):
                for j in range(boardik.h):
                    net[i][j] = 1
        else:
            net = None
        return net


class Guy(Figure):
    def __init__(self, x: int, y: int, team: alphabet.Team):
        move = [(-1, -1), (0, -1), (1, -1),
                (-1, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1)]
        attack = move
        capture = move
        charge = []

        # TODO change to new constructor of figure
        super(Guy, self).__init__('guy', alphabet.Place(x, y), 1, 1, -1, 1, 1,
                                  move, attack, capture, charge, team)


class Cat(Figure):  # Really strange piece
    def __init__(self, x: int, y: int, team: alphabet.Team):
        move = [(-2, -2), (0, -2), (2, -2),
            (-2, 0), (2, 0),
            (-2, 2), (0, 2), (2, 2)]

        attack = move[:]
        capture = move[:]
        charge = move[:]

        super(Cat, self).__init__(
            'cat', alphabet.Place(x, y), 2, 2, -1, 2, 2,
            {
                MoveType.MOVE: move,
                MoveType.ATTACK: attack,
                MoveType.CAPTURE: capture,
                MoveType.CHARGE: charge
            }, 
            team
        )


class King(Figure):
    def __init__(self, x: int, y: int, team: alphabet.Team):    
        move = [(-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)]
        attack = move
        capture = move
        charge = []

        super(King, self).__init__(team.name, alphabet.Place(x, y), 1, 1, -1, 1, 1,
                                   move, attack, capture, charge, team)


class Pawn(Figure):  # Buffed pawn, I will change it in next updates, maybe
    def __init__(self, x: int, y: int, team: alphabet.Team, direction: int):
        m = _direction(direction)
        move = [m]
        attack = []
        m1 = _direction(direction + 1)
        m2 = _direction(direction - 1)
        capture = [m1, m2]
        charge = []
        super(Pawn, self).__init__('pwn', alphabet.Place(x, y), 1, 1, direction, 1, 1,
                                   move, attack, capture, charge, team)


class Knight(Figure):
    def __init__(self, x: int, y: int, team: alphabet.Team):
        move = [(-1, -2), (1, -2),
            (-2, 1), (-2, -1), (2, 1), (2, -1),
            (-1, 2), (1, 2)]

        attack = []
        capture = move
        charge = []
    
        super(Knight, self).__init__('knt', alphabet.Place(x, y), 2, 2, -1, 3, 3,
                                     self.move, self.attack, self.capture, self.charge, team)


class Bishop(Figure):
    def __init__(self, x: int, y: int, team: alphabet.Team):
        move = []

        for i in range(1, 9):
            move.append((i, i))
            move.append((i, -i))
            move.append((-i, i))
            move.append((-i, -i))

        attack = []
        capture = move
        charge = []
    
        super(Bishop, self).__init__('bhp', alphabet.Place(x, y), 1, 1, -1, 8, 8,
                                     self.move, self.attack, self.capture, self.charge, team)


class Rook(Figure):
    def __init__(self, x: int, y: int, team: alphabet.Team):
        move = []

        for i in range(1, 9):
            move.append((0, i))
            move.append((0, -i))
            move.append((i, 0))
            move.append((-i, 0))

        attack = []
        capture = move
        charge = []

        super(Rook, self).__init__(
            'ruk', 
            alphabet.Place(x, y), 1, 1, -1, 8, 8,
            self.move, self.attack, self.capture, self.charge, team
        )


class Queen(Figure):
    def __init__(self, x: int, y: int, team: alphabet.Team):
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

        super(Queen, self).__init__('QUE', alphabet.Place(x, y), 1, 1, -1, 8, 8,
                                    self.move, self.attack, self.capture, self.charge, team)
