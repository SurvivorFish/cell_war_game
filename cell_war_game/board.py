from dataclasses import dataclass, field

import math
import alphabet
import figure
from colorama import Back
from colorama import Style


@dataclass
class Board:
    teams: list[str]
    width: int
    height: int
    cells: list[list[int]]
    
    figures: list[figure.Figure] = field(default_factory=list)
    step: int = field(default=0)
    
    def __post_init__(self):
        self.cells = [
            [-1 for _ in range(self.height)] 
            for _ in range(self.width)
        ]
        
    def _figure_name_at(self, place: alphabet.Place) -> str:
        figure_id = self.cells[place.x][place.y]
        if figure_id != -1:
            return self.figures[figure_id].name
        return '   '
        
    
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
            self.figures[f1].goto((x2, y2))
            if f2 != -1:  # if there is no second figure, it is just space and no need to change its place
                self.figures[f2].goto((x1, y1))
                self.names[x1][y1] = self.figures[f2].team.colour + self.figures[f2].name
            else:
                self.names[x1][y1] = "   "
            self.names[x2][y2] = self.figures[f1].team.colour + self.figures[f1].name

    # Next lines are printing the board

    def gap_count(self) -> int:
        return int(math.log10(self.h)) + 1

    def _separator(self) -> str:
        return '---'.join(['+'] * (self.w + 1))

    def _highlighted_separator(self, fr: int, to: int) -> str:  # Just separator with highlighting chosen place
        return '---'.join(['+'] * (fr - 1) + ['']) + '█████' * (to - fr) + '---'.join([''] + ['+'] * (self.w + 1 - to))

    def _header(self, lang: str) -> str:
        return '  ' + ' ' * self.gap_count() + '   '.join([alphabet.char(i, lang) for i in range(self.w)])
        # I already can't use map, because I added langs

    def _row(self, i: int) -> str:
        row_number = f'{i + 1:^{self.gap_count()}}'
        items = [row_number] + [self.names[j][i] + Style.RESET_ALL for j in range(self.w)]
        return '|'.join(items) + '|'

    def _highlighted_row(self, i: int, fr: int, to: int) -> str:
        row_number = f'{i + 1:^{self.gap_count()}}'
        items = [row_number] + [self.names[j][i] + Style.RESET_ALL for j in range(self.w)]
        first_items = items[:fr]
        highlighted_items = items[fr:to]
        last_items = items[to:]
        return '|'.join(first_items) + '█' + '█'.join(highlighted_items) + '█' + '|'.join(last_items) + '|'

    def print(self, lang: str, chosen_place: alphabet.Place = None):
        if chosen_place is None:
            print(self._header(lang))
            print(" " * self.gap_count() + (self._separator()))

            rows = [self._row(i) for i in range(self.h)]
            print(("\n" + " " * self.gap_count() + self._separator() + '\n').join(rows))

            print(" " * self.gap_count() + (self._separator() + '\n'))
        else:
            frX = chosen_place.x + 1
            toX = chosen_place.x + 1
            frY = chosen_place.y
            toY = chosen_place.y
            print(self._header(lang))
            if frY != 0:
                print(" " * self.gap_count() + (self._separator()))
                rows = [self._row(i) for i in range(0, frY)]
                print(("\n" + " " * self.gap_count() + self._separator() + '\n').join(rows))

            print(" " * self.gap_count() + (self._highlighted_separator(frX, toX + 1)))

            rows = [self._highlighted_row(i, frX, toX + 1) for i in range(frY, toY + 1)]
            print(("\n" + " " * self.gap_count() + self._highlighted_separator(frX, toX + 1) + '\n').join(rows))

            print(" " * self.gap_count() + (self._highlighted_separator(frX, toX + 1)))

            rows = [self._row(i) for i in range(toY + 1, self.h)]
            print(("\n" + " " * self.gap_count() + self._separator() + '\n').join(rows))

            if toY != self.h - 1:
                print(" " * self.gap_count() + (self._separator() + '\n'))
