# BM = base mechanics
bl = "湿"  # This letter was chosen by https://github.com/collapsedonion. It is not good to use more than 66 columns


# bl = broken letter. It shows up, when you use to many columns

def num(letter: str):
    if letter == "ё": return 6
    if letter == "Ё": return 39
    for i in range(0, 6):
        if letter == chr(ord("а") + i): return i
    for i in range(6, 32):
        if letter == chr(ord("а") + i): return i + 1
    for i in range(0, 6):
        if ord(letter) == ord("А") + i: return i + 33
    for i in range(6, 33):
        if ord(letter) == ord("А") + i: return i + 34
    return 66 + ord(letter) - ord(bl)


def char(number: int):  # designation in russian letters. Firstly - lowercase, then - uppercase
    if number <= 5:  # all before the ё
        return chr(ord("а") + number)
    if number == 6:  # the ё
        return "ё"
    if number <= 32:  # all before the end of russian alphabet
        return chr(ord("а") + number - 1)
    if number <= 38:  # uppercase before the Ё
        return chr(ord("А") + number - 33)
    if number == 39:  # the Ё
        return "Ё"
    if number <= 65:  # all before the end of russian alphabet but uppercase
        return chr(ord("А") + number - 34)
    return chr(
        ord(bl) + number - 66)


class Place:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, p):  # I hope, I'll use it in the future
        self.x += p.x
        self.y += p.y

    def sub(self, p):
        self.x -= p.x
        self.y -= p.y


class Team:
    def __init__(self, name: str, colour: str):  # colour - from colorama
        self.name = name
        self.colour = colour
