import math
import figure
import BM
from colorama import init, Fore
from colorama import Back
from colorama import Style


class board:
    h = 1
    w = 1
    cells = [[]]
    names = [[]]
    figures = []

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.names = [['   ' for x in range(height)] for y in range(width)]
        self.cells = [[-1 for x in range(height)] for y in range(width)]

    def addFigure(self, fgr):
        self.figures.append(fgr)
        x = fgr.place.x
        y = fgr.place.y
        self.cells[x][y] = len(self.figures) - 1
        self.names[x][y] = fgr.team.colour + fgr.name

    def move(self, x1, y1, x2, y2):
        if self.cells[x1][y1] == -1:
            print("Nu, i kogo mne dvigat")
            return
        if self.cells[x2][y2] == -1:
            f1 = self.cells[x1][y1]
            self.cells[x1][y1] = -1
            self.cells[x2][y2] = f1
            self.figures[f1].place = (x2, y2)
            self.names[x1][y1] = "   "
            self.names[x2][y2] = self.figures[f1].name
        else:
            f1 = self.cells[x1][y1]
            f2 = self.cells[x2][y2]
            self.cells[x1][y1] = f2
            self.cells[x2][y2] = f1
            self.figures[f1].place = (x2, y2)
            self.figures[f2].place = (x1, y1)
            self.names[x1][y1] = self.figures[f2].team.colour + self.figures[f2].name
            self.names[x2][y2] = self.figures[f1].team.colour + self.figures[f1].name

    def print(self, place = BM.place):
        if place.x == -1 and place.y == -1:
            probels = int(math.log10(self.h)) + 1
            s = probels * ' '
            for i in range(self.w):
                s += '  ' + BM.char(i) + ' '
            print(s)
            for i in range(2 * self.h + 1):
                s = ""

                if i % 2 == 0:
                    s += probels * ' '
                else:
                    s += (probels - int(math.log10((i + 1) / 2)) - 1) * ' ' + str((i) // 2 + 1)
                for j in range(2 * self.w + 1):
                    if i % 2 == 0:
                        if j % 2 == 0:
                            s += '+'
                        else:
                            s += '---'
                    elif j % 2 == 0:
                        s += '|'
                    else:
                        s += self.names[(j - 1) // 2][(i - 1) // 2]
                        s += Style.RESET_ALL
                print(s)



        else:
            this_figure = self.figures[self.cells[place.x][place.y]]
            probels = int(math.log10(self.h)) + 1
            s = probels * ' '
            for i in range(self.w):
                s += '  ' + BM.char(i) + ' '
            print(s)
            for i in range(2 * self.h + 1):
                s = ""

                if i % 2 == 0:
                    s += probels * ' '
                else:
                    s += (probels - int(math.log10((i + 1) / 2)) - 1) * ' ' + str((i) // 2 + 1)
                for j in range(2 * self.w + 1):
                    if i % 2 == 0:
                        if j % 2 == 0:
                            s += '+'
                        else:
                            s += '---'
                    elif j % 2 == 0:
                        s += '|'
                    else:
                        if (j - 1) // 2 == place.x and (i - 1) // 2 == place.y:
                            s += Back.BLACK + self.names[place.x][place.y] + Back.RESET#чёрный фон для выделения выделенной фигуры
                        else:
                            s += self.names[(j - 1) // 2][(i - 1) // 2]
                            s += Style.RESET_ALL
                print(s)
