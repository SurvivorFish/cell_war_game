# BM = base mechanics
first_letter = 1072


def num(char):
    return ord(char) - 1072


def char(integer):
    return chr(1072 + integer)


class place:
    place = []
    x = -1
    y = -1

    def __init__(self, x, y):
        self.place = [x, y]
        self.x = x
        self.y = y

    def add(self, move):
        self.place = [self.place[0] + move[0], self.place[1] + move[1]]


class team:
    name = 'NON'
    colour = ''

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
