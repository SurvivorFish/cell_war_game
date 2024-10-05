import figure
import board
import BM
from colorama import init, Fore
from colorama import Back
from colorama import Style



def move(from_cell, to_cell):
    x1 = BM.num(from_cell[0])
    y1 = int(from_cell[1:]) - 1
    x2 = BM.num(to_cell[0])
    y2 = int(to_cell[1:]) - 1
    boardik.move(x1, y1, x2, y2)


boardik = board.board(7, 9)

teams = []
teams.append(BM.team("RED", Fore.RED))
teams.append(BM.team("BLU", Fore.BLUE))

boardik.addFigure(figure.guy(5, 5, teams[0]))
boardik.addFigure(figure.cat(2, 2, teams[0]))
boardik.addFigure(figure.king(3, 8, teams[0]))

boardik.addFigure(figure.king(3, 0, teams[1]))


boardik.print()
end = False
while not end:
    inp = input()
    first_command = inp.split(" ")[0]
    commands = inp.split(" ")[1::]
    if first_command == "move":
        if len(commands) == 0 or commands[0] == "":
            print(Fore.RED + "Kavo?" + Style.RESET_ALL)
        elif len(commands) == 1:
            boardik.print(BM.place(BM.num(commands[0][0]), int(commands[0][1]) - 1))
        else:
            move(commands[0], commands[1])
            boardik.print()
    elif first_command == "print":
        boardik.print()
    elif first_command == "help":
        print('''move (from) (to) - moves figura from cell (from) to cell (to)
print - prints board again''')
    else:
        print("I dont know command " + first_command)
