import math
import BM
import figure
from colorama import Back
from colorama import Style


class Board:
    figures = []

    def __init__(self, width: int, height: int):  # creating a board
        self.w = width
        self.h = height
        self.names = [['   ' for _ in range(height)] for _ in range(width)]
        self.cells = [[-1 for _ in range(height)] for _ in range(width)]

    def add_figure(self, fgr: figure.Figure):  # adding a figure to the board
        self.figures.append(fgr)
        x = fgr.place.x
        y = fgr.place.y
        self.cells[x][y] = len(self.figures) - 1
        self.names[x][y] = fgr.team.colour + fgr.name

    def move(self, x1: int, y1: int, x2: int, y2: int):  # moving a figure
        if self.cells[x1][y1] == -1:  # if there is no figure to move, so ???
            print("???")
        else:
            f1 = self.cells[x1][y1]
            f2 = self.cells[x2][y2]
            self.cells[x1][y1] = f2
            self.cells[x2][y2] = f1
            self.figures[f1].place = (x2, y2)
            if f2 != -1: self.figures[f2].place = (x1, y1)  # if there is no second figure, no need to change its place
            if f2 != -1:  # if there is no second figure, it is just space
                self.names[x1][y1] = self.figures[f2].team.colour + self.figures[f2].name
            else:
                self.names[x1][y1] = "   "
            self.names[x2][y2] = self.figures[f1].team.colour + self.figures[f1].name

    def print(self, place_of_chosen_figure=BM.Place(-1, -1)):
        if place_of_chosen_figure.x == -1 and place_of_chosen_figure.y == -1:  # if no figures are chosen
            gaps = int(math.log10(self.h)) + 1  # number of gaps needed to make 
            s = gaps * ' '
            for i in range(self.w):
                s += '  ' + BM.char(i) + ' '
            print(s)
            for i in range(2 * self.h + 1):
                s = ""

                if i % 2 == 0:
                    s += gaps * ' '
                else:
                    s += (gaps - int(math.log10((i + 1) / 2)) - 1) * ' ' + str(i // 2 + 1)
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
        else:  # if some figure is chosen (now the only difference is next string and colored background)
            this_figure = self.figures[self.cells[place_of_chosen_figure.x][place_of_chosen_figure.y]]
            print(this_figure.name + " is chosen")  # just printing that figure is chosen
            gaps = int(math.log10(self.h)) + 1
            s = gaps * ' '
            for i in range(self.w):
                s += '  ' + BM.char(i) + ' '
            print(s)
            for i in range(2 * self.h + 1):
                s = ""

                if i % 2 == 0:
                    s += gaps * ' '
                else:
                    s += (gaps - int(math.log10((i + 1) / 2)) - 1) * ' ' + str(i // 2 + 1)
                for j in range(2 * self.w + 1):
                    if i % 2 == 0:
                        if j % 2 == 0:
                            s += '+'
                        else:
                            s += '---'
                    elif j % 2 == 0:
                        s += '|'
                    else:
                        if (j - 1) // 2 == place_of_chosen_figure.x and (i - 1) // 2 == place_of_chosen_figure.y:
                            s += Back.BLACK + self.names[place_of_chosen_figure.x][
                                place_of_chosen_figure.y] + Back.RESET  # Black background for highlighting
                        else:
                            s += self.names[(j - 1) // 2][(i - 1) // 2]
                            s += Style.RESET_ALL
                print(s)
