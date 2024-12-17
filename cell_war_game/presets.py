# Who needs json, when I don't know how to use it and I have Snakes language!
import board
import alphabet
import figure
from colorama import Fore
from colorama import Style


def preset_0(lst: list):
    teams = []
    boardik = board.Board(5, 5)
    teams += [alphabet.Team("RED", Fore.RED), alphabet.Team("BLU", Fore.BLUE)]
    # Red team
    boardik.add_figure(figure.Guy(2, 0, teams[0]))
    # Blue team
    boardik.add_figure(figure.King(2, 4, teams[1]))
    return boardik

def preset_1(lst: list):
    pass


_ALL_PRESETS = [
    preset_0,
    preset_1
]


def preset(number: int, lst: list):
    return _ALL_PRESETS[number](lst)
    
    # number = number of preset, teams = list of teams, lst = list of additional parameters
    if number == 0:  # Your preset
        # It is not good to use more than 66 columns. (You will see, why it is so).
        

    elif number == 1:  # Preset I used in the very beginning for testing
        boardik = board.Board(9, 9, teams)
        teams += [alphabet.Team("RED", Fore.RED), alphabet.Team("BLU", Fore.BLUE)]
        # Red team
        boardik.add_figure(figure.Guy(5, 5, teams[0]))
        boardik.add_figure(figure.Cat(2, 2, teams[0]))
        boardik.add_figure(figure.King(3, 8, teams[0]))
        # Blue team
        boardik.add_figure(figure.King(4, 0, teams[1]))

    elif number == 2:  # Two teams: king and row of guys
        boardik = board.Board(5, 5, teams)
        teams += [alphabet.Team("RED", Fore.RED), alphabet.Team("BLU", Fore.BLUE)]

        # Pawns
        for i in range(boardik.w):
            # Red team
            boardik.add_figure(figure.Guy(i, 1, teams[0]))
            # Blue team
            boardik.add_figure(figure.Guy(i, boardik.h - 2, teams[1]))

        # Kings
        # Red team
        boardik.add_figure(figure.King(boardik.w // 2, 0, teams[0]))
        # Blue team
        boardik.add_figure(figure.King(boardik.w // 2, boardik.h - 1, teams[1]))

    elif number == 3:  # Two teams: king, row of guys and two cats
        boardik = board.Board(5, 5, teams)
        teams += [alphabet.Team("RED", Fore.RED), alphabet.Team("BLU", Fore.BLUE)]

        # Pawns
        for i in range(boardik.w):
            # Red team
            boardik.add_figure(figure.Guy(i, 1, teams[0]))
            # Blue team
            boardik.add_figure(figure.Guy(i, boardik.h - 2, teams[1]))

        # Kings
        # Red team
        boardik.add_figure(figure.King(boardik.w // 2, 0, teams[0]))  # King
        boardik.add_figure(figure.Cat(boardik.w // 2 - 1, 0, teams[0]))  # Cat
        boardik.add_figure(figure.Cat(boardik.w // 2 + 1, 0, teams[0]))  # Cat
        # Blue team
        boardik.add_figure(figure.King(boardik.w // 2, boardik.h - 1, teams[1]))  # King
        boardik.add_figure(figure.Cat(boardik.w // 2 - 1, boardik.h - 1, teams[1]))  # Cat
        boardik.add_figure(figure.Cat(boardik.w // 2 + 1, boardik.h - 1, teams[1]))  # Cat

    elif number == 4:  # Chess!!!
        boardik = board.Board(8, 8, teams)
        teams += [alphabet.Team("WHT", Fore.WHITE), alphabet.Team("BLC", Fore.BLACK)]

        # Pawns
        for i in range(boardik.w):
            # Black team
            boardik.add_figure(figure.Pawn(i, 6, teams[1], 2))
            # White team
            boardik.add_figure(figure.Pawn(i, 1, teams[0], 6))

        # White team
        boardik.add_figure(figure.King(3, 0, teams[0]))
        boardik.add_figure(figure.Queen(4, 0, teams[0]))
        boardik.add_figure(figure.Bishop(5, 0, teams[0]))
        boardik.add_figure(figure.Bishop(2, 0, teams[0]))
        boardik.add_figure(figure.Knight(1, 0, teams[0]))
        boardik.add_figure(figure.Knight(6, 0, teams[0]))
        boardik.add_figure(figure.Rook(0, 0, teams[0]))
        boardik.add_figure(figure.Rook(7, 0, teams[0]))

        # Black team
        boardik.add_figure(figure.King(3, 7, teams[1]))
        boardik.add_figure(figure.Queen(4, 7, teams[1]))
        boardik.add_figure(figure.Bishop(5, 7, teams[1]))
        boardik.add_figure(figure.Bishop(2, 7, teams[1]))
        boardik.add_figure(figure.Knight(1, 7, teams[1]))
        boardik.add_figure(figure.Knight(6, 7, teams[1]))
        boardik.add_figure(figure.Rook(0, 7, teams[1]))
        boardik.add_figure(figure.Rook(7, 7, teams[1]))

    else:  # Sandbox?
        boardik = board.Board(21, 21, teams)
        teams += [alphabet.Team("RED", Fore.RED)]
        boardik.add_figure(figure.King(10, 10, teams[0]))

        teams += [alphabet.Team("WHT", Fore.WHITE), alphabet.Team("BLC", Fore.BLACK)]
        boardik.add_figure(figure.King(13, 13, teams[1]))
        boardik.add_figure(figure.King(14, 14, teams[2]))

        boardik.add_figure(figure.Cat(13, 11, teams[0]))

    return boardik


def my_preset(teams: list):
    # It is not good to use more than 66 columns. (You will see, why it is so).
    boardik = board.Board(5, 5, teams)
    teams += [alphabet.Team("RED", Fore.RED), alphabet.Team("BLU", Fore.BLUE)]
    # Red team
    boardik.add_figure(figure.Guy(2, 0, teams[0]))
    # Blue team
    boardik.add_figure(figure.King(2, 4, teams[1]))
    return boardik


def load_game():
    return 1
