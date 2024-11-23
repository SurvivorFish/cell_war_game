import figure
import board
import alphabet
from colorama import Fore
from colorama import Style


def test_designation():  # Just small test of designation of columns
    for i in range(0, 100):
        ch = alphabet.char(i, "ru")
        print(str(alphabet.num(ch, "ru")) + " " + ch)


def move(from_cell: str, to_cell: str, language: str):  # cells are added like user sees it
    x1 = alphabet.num(from_cell[0], language)
    y1 = int(from_cell[1:]) - 1
    x2 = alphabet.num(to_cell[0], language)
    y2 = int(to_cell[1:]) - 1
    boardik.move(x1, y1, x2, y2)


# import settings
_settings_file_ = open('cell_war_game/settings.txt', 'r')
default_lang = 'en'
ask_lang = 0
use_terminal = 1

for i in _settings_file_.read().split('\n'):
    if 'default_lang:' in i:
        default_lang = i.split('default_lang:')[-1].strip()
    if 'ask_lang:' in i:
        ask_lang = (int(i.split('ask_lang:')[-1].strip()) == 1)
    if 'use_terminal:' in i:
        use_terminal = bool(int(i.split('use_terminal:')[-1].strip()) == 1)
_settings_file_.close()


boardik = board.Board(7, 7)
# It is not good to use more than 66 columns. (You will see, why it is so).

teams = [alphabet.Team("RED", Fore.RED), alphabet.Team("BLU", Fore.BLUE)]
available_langs = ["ru", "en"]
langs = []


if ask_lang:
    while len(langs) < len(teams):  # Choosing language for each team
        print("Choose language for " + teams[len(langs)].name + " team (ru or en)")
        lang = input()
        if lang in available_langs:
            langs.append(lang)
        elif lang == "":
            langs.append(default_lang)
        else:
            print("I don't know " + lang + " language")
else:
    while len(langs) < len(teams):
        langs.append(default_lang)


preset = 2

if preset == 0:
    # Red team
    boardik.add_figure(figure.Guy(5, 5, teams[0]))
    boardik.add_figure(figure.Cat(2, 2, teams[0]))
    boardik.add_figure(figure.King(3, 8, teams[0]))
    # Blue team
    boardik.add_figure(figure.King(4, 0, teams[1]))

elif preset == 1:
    # Pawns
    for i in range(boardik.w):
        # Red team
        boardik.add_figure(figure.Guy(i, 1, teams[0]))
        # Blue team
        boardik.add_figure(figure.Guy(i, boardik.h-2, teams[1]))

    # Kings
    # Red team
    boardik.add_figure(figure.King(boardik.w//2, 0, teams[0]))
    # Blue team
    boardik.add_figure(figure.King(boardik.w//2, boardik.h-1, teams[1]))

elif preset == 2:
    # Pawns
    for i in range(boardik.w):
        # Red team
        boardik.add_figure(figure.Guy(i, 1, teams[0]))
        # Blue team
        boardik.add_figure(figure.Guy(i, boardik.h-2, teams[1]))

    # Kings
    # Red team
    boardik.add_figure(figure.King(boardik.w//2, 0, teams[0]))
    boardik.add_figure(figure.Cat(boardik.w//2-1, 0, teams[0]))
    boardik.add_figure(figure.Cat(boardik.w//2+1, 0, teams[0]))
    # Blue team
    boardik.add_figure(figure.King(boardik.w//2, boardik.h-1, teams[1]))
    boardik.add_figure(figure.Cat(boardik.w//2-1, boardik.h-1, teams[1]))
    boardik.add_figure(figure.Cat(boardik.w//2+1, boardik.h-1, teams[1]))

elif preset == 3:
    # an error occured, so I made asdjhnfjkdsfgbj

    boardik.add_figure(figure.King(boardik.w // 2, 0, teams[0]))
    # Blue team
    boardik.add_figure(figure.King(boardik.w // 2, boardik.h - 1, teams[1]))
    boardik.add_figure(figure.Cat(boardik.w // 2 - 1, boardik.h - 1, teams[1]))
    boardik.add_figure(figure.Cat(boardik.w // 2 + 3, boardik.h - 1, teams[1]))

    for i in range(2):
        boardik.add_figure(figure.Guy(4+i, 4, teams[0]))
        boardik.add_figure(figure.Guy(i, 9, teams[1]))
        boardik.add_figure(figure.Guy(9+i, 9, teams[1]))

    for i in range(3):
        boardik.add_figure(figure.Guy(8+i, 1, teams[0]))

    for i in range(5):
        boardik.add_figure(figure.Guy(3+i, 8, teams[1]))

    boardik.add_figure(figure.Guy(3, 5, teams[0]))
    boardik.add_figure(figure.Guy(6, 5, teams[0]))
    boardik.add_figure(figure.Guy(0, 1, teams[0]))
    boardik.add_figure(figure.Guy(2, 3, teams[0]))
    boardik.add_figure(figure.Guy(5, 1, teams[0]))

else:
    boardik.add_figure(figure.King(0, 0, teams[0]))

end = False  # Just flag for stopping the game
step = 0  # step is value that means team with number step will start first
last_step = -1
boardik.print(langs[step])
while not end:
    if teams[step].lose:
        last_step = step - 1
    while teams[step].lose:
        step = (step + 1) % len(teams)

    if step == last_step: #this means, that only one team left
        end = True
        print(f'THE {teams[step].colour + teams[step].name + Style.RESET_ALL} is winner!!!')
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
        continue



    print("Now team " + str(teams[step].name + " is making a move"))
    inp = input()
    first_command = inp.split(" ")[0]
    commands = inp.split(" ")[1::]
    if first_command == "move" or first_command == "capture" or first_command == "attack" or first_command == "charge":
        if first_command == "move": type_of_move = 0
        elif first_command == "capture": type_of_move = 1
        elif first_command == "attack": type_of_move = 2
        else: type_of_move = 3

        if len(commands) == 0 or commands[0] == "":
            print(Fore.RED + "Kavo?" + Style.RESET_ALL)

        elif len(commands) == 1:
            f = alphabet.Place(alphabet.num(commands[0][0], langs[step]), int(commands[0][1:]) - 1)

            if not (0 <= f.x < boardik.w and 0 <= f.y < boardik.h):
                print("This place is outside the board")
                continue
            if boardik.cells[f.x][f.y] == -1:
                print("there is no piece on this place")
                continue

            boardik.print(langs[step], f)

        elif len(commands) == 2 or (len(commands) == 3 and commands[2] == ""):
            if type_of_move == 3:
                print('Type "help" to understand what charge mean')
                continue
            # p1 and p2 are places, not figures!
            p1 = alphabet.Place(alphabet.num(commands[0][0], langs[step]), int(commands[0][1::]) - 1)
            p2 = alphabet.Place(alphabet.num(commands[1][0], langs[step]), int(commands[1][1::]) - 1)

            # Special cases
            if not (0 <= p1.x < boardik.w or 0 <= p1.y < boardik.h):
                print("First place is outside the board")       # p1 outside the board
                continue
            if not (0 <= p2.x < boardik.w and 0 <= p2.y < boardik.h):
                print("Second place is outside the board")      # p2 outside the board
                continue
            if boardik.cells[p1.x][p1.y] == -1:
                print("there is no piece on this place")        # No p1?
                continue

            if boardik.cells[p2.x][p2.y] == -1:  # is p2 a gap?
                if type_of_move == 1 or type_of_move == 2:
                    print("I can't attack non-existing figure")
                    continue

                if not (alphabet.Place(p2.x, p2.y) - alphabet.Place(p1.x, p1.y)
                        in boardik.figures[boardik.cells[p1.x][p1.y]].moves):
                    print(boardik.figures[boardik.cells[p1.x][p1.y]].name + " can't move there")
                    continue        # p1 can't move to place p2
                if boardik.figures[boardik.cells[p1.x][p1.y]].team != teams[step]:
                    print("you can't move other players' pieces")  # this piece isn't yours
                    continue

                # move piece to another place
                move(commands[0], commands[1], langs[step])
                step = (step + 1) % len(teams)
                boardik.print(langs[step])
            else:   # if p2 is a figure
                if not (alphabet.Place(p2.x, p2.y) - alphabet.Place(p1.x, p1.y)
                        in boardik.figures[boardik.cells[p1.x][p1.y]].moves):
                    print(boardik.figures[boardik.cells[p1.x][p1.y]].name + " can't move there")
                    continue        # p1 can't move to place p2
                if type_of_move == 0:  # if player want to move figure
                    if boardik.figures[boardik.cells[p1.x][p1.y]].team != teams[step] \
                            or boardik.figures[boardik.cells[p2.x][p2.y]].team != teams[step]:
                        print("You can't move other players' pieces")  # one of the pieces isn't yours
                        continue

                    move(commands[0], commands[1], langs[step])
                    step = (step + 1) % len(teams)
                    boardik.print(langs[step])

                else:  # if player want to attack or capture
                    if boardik.figures[boardik.cells[p1.x][p1.y]].team != teams[step]:
                        print("Do you really want another player's piece to attack?")
                        continue
                    if boardik.figures[boardik.cells[p2.x][p2.y]].team == teams[step]:
                        print("Do you want to attack your own piece? What a dishonor!")
                        continue

                    # this means that this piece is king
                    if boardik.figures[boardik.cells[p2.x][p2.y]].name == \
                            boardik.figures[boardik.cells[p2.x][p2.y]].team.name:
                        for i in teams:
                            if boardik.figures[boardik.cells[p2.x][p2.y]].team == i:
                                i.lose = True

                    boardik.cells[p2.x][p2.y] = -1
                    boardik.names[p2.x][p2.y] = "   "
                    # Let's not remove prey from figures array (it will be easier to make)

                    if type_of_move == 1:
                        move(commands[0], commands[1], langs[step])
                    step = (step + 1) % len(teams)
                    boardik.print(langs[step])
        elif type_of_move == 3 and len(commands) == 3 or (len(commands) == 4 and commands[3] == ""):
            # "
            p1 = alphabet.Place(alphabet.num(commands[0][0], langs[step]), int(commands[0][1::]) - 1)
            p2 = alphabet.Place(alphabet.num(commands[1][0], langs[step]), int(commands[1][1::]) - 1)
            p3 = alphabet.Place(alphabet.num(commands[2][0], langs[step]), int(commands[2][1::]) - 1)
            # Разум заперт изнутри" - Атомное сердце)

            if boardik.figures[boardik.cells[p1.x][p1.y]].team != teams[step]:
                print("You can't charge with other players' pieces")
                continue
            if boardik.figures[boardik.cells[p3.x][p3.y]].team == teams[step]:
                print("Do you want to attack your own piece? What a dishonor!")
                continue
            if boardik.cells[p2.x][p2.y] != -1:
                print(f"There is a piece on {commands[1]}. It interrupts my charge!")
                continue

            if not (alphabet.Place(p2.x, p2.y) - alphabet.Place(p1.x, p1.y)
                    in boardik.figures[boardik.cells[p1.x][p1.y]].moves):
                print(boardik.figures[boardik.cells[p1.x][p1.y]].name + " can't move there")
                continue  # p1 can't move to place p2

            if not (alphabet.Place(p3.x, p3.y) - alphabet.Place(p2.x, p2.y)
                    in boardik.figures[boardik.cells[p1.x][p1.y]].moves):
                print(boardik.figures[boardik.cells[p1.x][p1.y]].name + " can't attack there")
                continue  # p1 can't attack (for now it's = move) to place p2

            # this means that this piece is king
            if boardik.figures[boardik.cells[p3.x][p3.y]].name == \
                    boardik.figures[boardik.cells[p3.x][p3.y]].team.name:
                for i in teams:
                    if boardik.figures[boardik.cells[p3.x][p3.y]].team == i:
                        i.lose = True

            boardik.cells[p3.x][p3.y] = -1
            boardik.names[p3.x][p3.y] = "   "
            # Let's not remove prey from figures array (it will be easier to make)

            move(commands[0], commands[1], langs[step])
            step = (step + 1) % len(teams)
            boardik.print(langs[step])
        else:
            print("This command has only 2 arguments")
    elif first_command == "print":
        boardik.print(langs[step])
    elif first_command == "help":
        print('''move (from) (to) - moves figura from cell (from) to cell (to)
attack (from) (to) - attack another player's figure, but don't capture it's place
capture (from) (to) - attack another player's figure and capture it's place
charge (from) (to) (attack) - capture empty place and attack another player's figure
print - prints board again
skip - skip your turn''')
    elif first_command == "skip":
        step = (step + 1) % len(teams)
        boardik.print(langs[step])
    else:
        print("I dont know command " + first_command)
