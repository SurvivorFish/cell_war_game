# BM = base mechanics
import sys

_bl_ = "湿"  # This letter was chosen by https://github.com/collapsedonion. It is not good to use more than 66 columns
# bl = broken letter. It shows up, when you use to many columns
_RU_ALPHABET_ = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# designation in russian letters. Firstly - lowercase, then - uppercase
# _EN_ALPHABET_ = "abvgdeёjziyklmnoprstufhcчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# haven't found all the letters... TnT
_EN_ALPHABET_ = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# designation in english letters. Firstly - lowercase, then - uppercase


__HELP_MESSAGE__ = '''move (from) (to) - moves figura from cell (from) to cell (to)
attack (from) (to) - attack another player's figure, but don't capture it's place
capture (from) (to) - attack another player's figure and capture it's place
charge (from) (to) (attack) - capture empty place and attack another player's figure
print - prints board again
skip - skip your turn'''


def num(letter: str, lang: str) -> int:
    if lang == "en":
        if letter in _EN_ALPHABET_: return _EN_ALPHABET_.index(letter)
        return len(_EN_ALPHABET_) + ord(letter) - ord(_bl_)
    elif lang == "ru":
        if letter in _RU_ALPHABET_: return _RU_ALPHABET_.index(letter)
        return len(_RU_ALPHABET_) + ord(letter) - ord(_bl_)
    else:
        try:
            asdhkj = int("asdhkj")
        except ValueError:
            print("Oy... You tried to take wrong language")  # Just want to point an error don't know how to do iy well
            sys.exit()


def char(index: int, lang: str):
    if lang == "en":
        if index < len(_EN_ALPHABET_): return _EN_ALPHABET_[index]
        return chr(ord(_bl_) + index - len(_EN_ALPHABET_))
    elif lang == "ru":
        if index < len(_RU_ALPHABET_): return _RU_ALPHABET_[index]
        return chr(ord(_bl_) + index - len(_RU_ALPHABET_))
    else:
        try:
            asdhkj = int("asdhkj")
        except ValueError:
            print("Oy... You tried to take wrong language")
            sys.exit()


def draw_pony():
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠗⢤⡀⠀⠀⠀⠀⠀⠀⠀⣰⢶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣠⠴⠖⢏⣉⣉⣹⠀⠀⢹⢦⡀⠀⠀⡰⣆⢠⠃⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣠⡶⠋⠁⢀⡴⠚⠉⠀⠀⠁⠀⠘⡎⣷⣄⠀⠇⢸⡎⢀⡇⣤⣄⠀⠀⢀⡤⠶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡴⢛⡠⠶⢶⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣾⣶⠀⢸⠀⢸⣾⠞⢹⡤⠚⠁⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⡗⠉⠀⠀⣾⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠹⡿⣧⠀⢀⡾⠁⠐⠋⠀⢀⣴⣋⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⡀⠀⡔⠉⢻⠀⠸⡏⢍⣿⣖⠺⡷⠤⠆⠀⠀⢹⣾⡀⣾⠖⡆⠀⠠⠔⠋⠁⣀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢧⠀⣇⠀⠈⠣⡀⠙⢌⣿⣿⣿⠇⠀⠀⠀⠀⠀⢿⣿⡼⠀⣧⢤⡄⡠⠴⠮⠥⣄⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠈⢷⣜⣆⠀⢀⡅⠀⠀⠈⠉⠀⢀⡴⠀⠀⠀⠀⢸⡇⡇⠈⠁⣼⣁⣤⠤⠒⢊⠥⠒⠊⠉⠉⠉⠉⠙⠻⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠙⢿⣷⣬⣳⠤⠴⠤⡖⠊⢁⣿⠀⠀⠀⠀⠈⡿⠁⠀⢚⣏⠵⠈⢲⣊⠥⠒⠒⠒⠒⠤⢄⡀⠀⠀⠀⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⢿⣌⠑⢆⢠⠇⢠⡞⢸⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢘⡏⠉⠉⠉⠑⢦⡀⠀⠈⠓⣄⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣰⡾⠳⠀⡏⠇⢈⡟⣴⠋⠀⡼⣄⠀⠀⠀⠀⠀⠀⢆⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠹⡄⠀⠀⠈⡆⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢫⡻⠤⠔⢃⡶⢋⡞⢁⠤⠊⠀⢸⠦⡌⠀⠀⣖⣀⣨⣦⡀⠀⢀⣎⡀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⢸⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⠉⠉⠁⠀⡾⠊⣁⠠⠤⢒⣻⡟⠀⠀⡴⠃⠀⠀⢳⠙⡄⠀⠀⢳⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⡎⠀⢀⡜⡟⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⡡⠊⠀⣠⠖⠋⣼⣤⠀⢸⢳⠀⠀⠀⠀⡇⠸⡀⠀⠀⣇⠀⠀⠀⣠⠋⠀⠀⢀⠞⢀⡠⠋⡜⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⡾⠓⢶⠀⢻⢙⣖⠈⠛⠦⡄⠀⠀⢸⠀⡇⠀⠀⢸⡀⢀⡼⠁⠀⣠⣖⡡⠔⢉⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⠝⠶⠟⠀⢸⢿⡀⠀⠀⢠⠃⠀⠀⡜⠀⡇⠀⠀⠈⡇⡾⠁⡰⡻⠊⠁⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣀⣱⣄⣠⡏⠀⠀⠰⠧⣴⠁⠀⠀⢀⡇⢷⣸⠀⡁⠀⠀⠛⠲⠴⠒⠒⠒⣲⣦⣑⢲⡦⣄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠙⠲⠧⠤⠤⠤⠤⠔⠒⠊⠉⠁⢀⡄⠈⠹⡌⢇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣤⢤⣜⠡⠊
                """)


class Place:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _add_tuple(self, p: tuple):  # I hope, I'll use it in the future
        return Place(self.x + p[0], self.y + p[1])

    def __add__(self, other):
        if isinstance(other, tuple): 
            other = Place(*other)
        if isinstance(other, Place): 
            return Place(self.x + other.x, self.y + other.y)
        return

    def __sub__(self, other):
        if isinstance(other, Place): return Place(self.x - other.x, self.y - other.y)
        if isinstance(other, tuple): return self._add_tuple((-other[0], -other[1]))
        return

    def __eq__(self, other):
        if isinstance(other, Place): return self.x == other.x and self.y == other.y
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        else:
            return


class Team:
    def __init__(self, name: str, colour: str):  # colour - from colorama
        self.name = name
        self.colour = colour
        self.lose = False


if __name__ == '__main__':
    p1 = Place(1, 2)
    # вместо p1 + (2, 3)
    p1 + Place(2, 3)