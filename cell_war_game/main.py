import figure
import board
import BM
from colorama import Fore
from colorama import Style


def test_designation():  # Just small test of designation of columns
    for i in range(0, 100):
        ch = BM.char(i)
        print(str(BM.num(ch)) + " " + ch)


def move(from_cell: str, to_cell: str):  # cells are added like user sees it
    x1 = BM.num(from_cell[0])
    y1 = int(from_cell[1:]) - 1
    x2 = BM.num(to_cell[0])
    y2 = int(to_cell[1:]) - 1
    boardik.move(x1, y1, x2, y2)


boardik = board.Board(100, 9)  # It is not good to use more than 66 columns. (You will see, why it is so).

teams = [BM.Team("RED", Fore.RED), BM.Team("BLU", Fore.BLUE)]

# Red team
boardik.add_figure(figure.Guy(5, 5, teams[0]))
boardik.add_figure(figure.Cat(2, 2, teams[0]))
boardik.add_figure(figure.King(3, 8, teams[0]))
# Blue team
boardik.add_figure(figure.King(3, 0, teams[1]))

boardik.print()
end = False
step = 0
while not end:
    print("Now team " + str(teams[step].name + " is making a move"))
    inp = input()
    first_command = inp.split(" ")[0]
    commands = inp.split(" ")[1::]
    if first_command == "move":
        if len(commands) == 0 or commands[0] == "":
            print(Fore.RED + "Kavo?" + Style.RESET_ALL)
        elif len(commands) == 1:
            f = BM.Place(BM.num(commands[0][0]), int(commands[0][1::]) - 1)
            if boardik.cells[f.x][f.y] == -1:
                print("there is no piece on this place")
            elif boardik.figures[boardik.cells[f.x][f.y]].team != teams[step]:
                print("you can't move other players' pieces")
            else:
                boardik.print(BM.Place(BM.num(commands[0][0]), int(commands[0][1]) - 1))
        elif len(commands) == 2:
            f1 = BM.Place(BM.num(commands[0][0]), int(commands[0][1::]) - 1)
            f2 = BM.Place(BM.num(commands[1][0]), int(commands[1][1::]) - 1)
            if boardik.cells[f1.x][f1.y] == -1:
                print("there is no piece on this place")
            elif boardik.cells[f2.x][f2.y] == -1:
                move(commands[0], commands[1])
                step = (step + 1) % len(teams)
                boardik.print()
            elif boardik.figures[boardik.cells[f1.x][f1.y]].team != teams[step] \
                    or boardik.figures[boardik.cells[f2.x][f2.y]].team != teams[step]:
                print("you can't move other players' pieces")
            else:
                move(commands[0], commands[1])
                step = (step + 1) % len(teams)
                boardik.print()
        else:
            print("Command move has only 2 arguments")
    elif first_command == "print":
        boardik.print()
    elif first_command == "help":
        print('''move (from) (to) - moves figura from cell (from) to cell (to)
print - prints board again''')
    else:
        print("I dont know command " + first_command)
