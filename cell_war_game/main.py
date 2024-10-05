import figure
import board


def move(from_cell, to_cell):
    x1 = ord(from_cell[0]) - 1072
    y1 = int(from_cell[1:]) - 1
    x2 = ord(to_cell[0]) - 1072
    y2 = int(to_cell[1:]) - 1
    boardik.move(x1, y1, x2, y2)


boardik = board.board(7, 9)
boardik.addFigure(figure.guy(5, 5))
boardik.addFigure(figure.cat(2, 2))

boardik.print()

end = False
while (not end):
    inp = input()
    first_command = inp.split(" ")[0]
    commands = inp.split(" ")[1::]
    if first_command == "move":
        move(commands[0], commands[1])
        boardik.print()
    elif first_command == "print":
        boardik.print()
    elif first_command == "help":
        print('''move (from) (to) - moves figura from cell (from) to cell (to)
print - prints board again''')
    else:
        print("I dont know command " + first_command)
