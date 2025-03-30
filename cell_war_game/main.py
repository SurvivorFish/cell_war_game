from datetime import datetime
import json
from dataclasses import dataclass
import dill
import alphabet
import presets_JSON
from colorama import Fore
from colorama import Style


def test_designation():  # Just small test of designation of columns
    for j in range(0, 100):
        ch = alphabet.char(j, "ru")
        print(str(alphabet.num(ch, "ru")) + " " + ch)


def move(from_cell: str, to_cell: str, language: str):  # cells are added like user sees it
    x1 = alphabet.num(from_cell[0], language)
    y1 = int(from_cell[1:]) - 1
    x2 = alphabet.num(to_cell[0], language)
    y2 = int(to_cell[1:]) - 1
    boardik.move(x1, y1, x2, y2)


def import_langs(tms: list):
    languages = []  # tms = teams
    while len(languages) < len(tms):  # Choosing language for each team
        print("Choose language for " + tms[len(langs)].name + " team (ru or en)")
        lang = input()
        if lang in available_langs:
            languages.append(lang)
        elif lang == "":
            languages.append(default_lang)
        else:
            print("I don't know " + lang + " language")
    return languages


# Settings dataclass
@dataclass
class Settings:
    default_lang: str
    ask_lang: bool
    use_terminal: bool
    recording: bool
    start_from_preset: bool


@dataclass
class SomeItem:
    item_id: int
    owner_id: int
    name: str
    description: str
    price: int


# importing settings
try:  # I have main and main (1), don't know, which is real
    with open('cell_war_game/resources/settings.json', encoding='utf-8') as fd:
        json_item = json.load(fd)
        settings = Settings(**json_item)
except Exception as e:
    print('ignore this' + str(e))
    with open('resources/settings.json', encoding='utf-8') as fd:
        json_item = json.load(fd)
        settings = Settings(**json_item)
default_lang = settings.default_lang
ask_lang = settings.ask_lang
use_terminal = settings.use_terminal
recording = settings.recording
start_from_preset = settings.start_from_preset

if start_from_preset:
    # Game presets (teams, colours, pieces)
    preset = 4
    boardik = presets_JSON.preset(preset, [])
else:
    print("Please, write the save file")
    loaded_file = input()
    try:  # I have main and main (1), don't know, which is real
        with open("saves/" + loaded_file, 'rb') as fd:
            boardik = dill.load(fd, encoding='utf-8')
    except Exception as e:
        print('ignore this' + str(e))
        with open("cell_war_game/saves/" + loaded_file, 'rb') as fd:
            boardik = dill.load(fd, encoding='utf-8')

# Language selection (only names of columns)
available_langs = ["ru", "en"]
langs = []
if ask_lang:
    langs = import_langs(boardik.teams)
else:
    while len(langs) < len(boardik.teams):
        langs.append(default_lang)

# Naming this game in save file
save_name = "save_" + "-".join("-".join("-".join(str(datetime.now()).split(" ")).split(":")).split(".")) + ".cwg_sav"

# Main loop
end = False  # Just flag for stopping the game
boardik.print(langs[boardik.step])
while not end:

    # SAVING
    try:  # I have main and main (1), don't know, which is real
        with open("saves/" + save_name, 'wb') as fd:
            dill.dump(boardik, fd)
    except Exception as e:
        print('ignore this' + str(e))
        with open("cell_war_game/saves/" + save_name, 'wb') as fd:
            dill.dump(boardik, fd)

    # WIN?
    WINNER = -1
    end = True
    for team in boardik.teams:
        if WINNER == -1:
            if not team.lose:
                WINNER = boardik.teams.index(team)
        elif WINNER != -1 and team != boardik.teams[WINNER]:
            if not team.lose:
                end = False
    if end:
        print(f'THE {boardik.teams[WINNER].colour + boardik.teams[WINNER].name + Style.RESET_ALL}'
              f' is winner!!!')
        alphabet.draw_pony()
        continue

    # SKIP LEFT TEAMS
    while boardik.teams[boardik.step].lose:
        boardik.step = (boardik.step + 1) % len(boardik.teams)

    # READ COMMAND
    print("Now team " + str(boardik.teams[boardik.step].name + " is making a move"))
    inp = input()
    first_command = inp.split(" ")[0]
    commands = inp.split(" ")[1::]

    # SOME KIND OF SWITCH CASE
    # "MOVE" commands
    if first_command == "move" or first_command == "capture" or first_command == "attack" or first_command == "charge":

        # type of move determination
        if first_command == "move":
            type_of_move = 0
        elif first_command == "capture":
            type_of_move = 1
        elif first_command == "attack":
            type_of_move = 2
        else:
            type_of_move = 3

        if len(commands) == 0 or commands[0] == "":
            print(Fore.RED + "Kavo?" + Style.RESET_ALL)

        elif len(commands) == 1:
            f = alphabet.Place(alphabet.num(commands[0][0], langs[boardik.step]), int(commands[0][1:]) - 1)

            if not (0 <= f.x < boardik.w and 0 <= f.y < boardik.h):
                print("This place is outside the board")
                continue
            if boardik.cells[f.x][f.y] == -1:
                print("there is no piece on this place")
                continue

            boardik.print(langs[boardik.step], f)

        elif len(commands) == 2 or (len(commands) == 3 and commands[2] == ""):
            if type_of_move == 3:
                print('Type "help" to understand what charge mean')
                continue

            # p1 and p2 are places, not figures!
            p1 = alphabet.Place(alphabet.num(commands[0][0], langs[boardik.step]), int(commands[0][1::]) - 1)
            p2 = alphabet.Place(alphabet.num(commands[1][0], langs[boardik.step]), int(commands[1][1::]) - 1)
            # f1 and f2 are figures
            f1 = boardik.figures[boardik.cells[p1.x][p1.y]]
            f2 = boardik.figures[boardik.cells[p2.x][p2.y]]

            # special cases
            if not (0 <= p1.x < boardik.w or 0 <= p1.y < boardik.h):
                print("First place is outside the board")  # p1 outside the board
                continue
            if not (0 <= p2.x < boardik.w and 0 <= p2.y < boardik.h):
                print("Second place is outside the board")  # p2 outside the board
                continue
            if boardik.cells[p1.x][p1.y] == -1:
                print("there is no piece on this place")  # No p1?
                continue

            # jumping into space
            if boardik.cells[p2.x][p2.y] == -1:  # is p2 a gap?
                if type_of_move == 1 or type_of_move == 2:
                    print("I can't attack non-existing figure")
                    continue

                if (not p2 - p1 in f1.move) or (not f1.can('move', boardik)[p2.x][p2.y] > 0):
                    print(f1.name + " can't move there")
                    continue  # p1 can't move to place p2
                if f1.team != boardik.teams[boardik.step]:
                    print("you can't move other players' pieces")  # this piece isn't yours
                    continue

                # move piece to another place
                move(commands[0], commands[1], langs[boardik.step])
                boardik.step = (boardik.step + 1) % len(boardik.teams)
                boardik.print(langs[boardik.step])

            # swapping or attacking figures
            else:  # if p2 is a figure
                # move command = swamp
                if type_of_move == 0:
                    if (not p2 - p1 in f1.move) or (not f1.can('move', boardik)[p2.x][p2.y] > 0):
                        print(f1.name + " can't move there")
                        continue  # p1 can't move to place p2

                    # special case
                    if f1.team != boardik.teams[boardik.step] or f2.team != boardik.teams[boardik.step]:
                        print("You can't move other players' pieces")
                        continue

                    move(commands[0], commands[1], langs[boardik.step])
                    boardik.step = (boardik.step + 1) % len(boardik.teams)
                    boardik.print(langs[boardik.step])

                # attack or capture
                else:  # if player want to attack or capture
                    if type_of_move == 1:
                        if (not p2 - p1 in f1.capture) or (not f1.can('capture', boardik)[p2.x][p2.y] > 0):
                            print(f1.name + " can't capture there")
                            continue  # p1 can't move to place p2
                    else:
                        if (not p2 - p1 in f1.attack) or (not f1.can('attack', boardik)[p2.x][p2.y] > 0):
                            print(f1.name + " can't attack there")
                            continue  # p1 can't move to place p2

                    if f1.team != boardik.teams[boardik.step]:
                        print("Do you really want another player's piece to attack?")
                        continue
                    if f2.team == boardik.teams[boardik.step]:
                        print("Do you want to attack your own piece? What a dishonor!")
                        continue

                    # this means that this piece is king
                    # if team lose its king, the team is losing
                    if f2.name == f2.team.name:
                        for i in boardik.teams:
                            if f2.team == i:
                                i.lose = True
                                continue

                    boardik.cells[p2.x][p2.y] = -1
                    boardik.names[p2.x][p2.y] = "   "
                    # Let's not remove prey from figures array (it will be easier to make)

                    if type_of_move == 1:
                        move(commands[0], commands[1], langs[boardik.step])
                    boardik.step = (boardik.step + 1) % len(boardik.teams)
                    boardik.print(langs[boardik.step])

        # charge
        elif type_of_move == 3 and len(commands) == 3 or (len(commands) == 4 and commands[3] == ""):
            # "
            p1 = alphabet.Place(alphabet.num(commands[0][0], langs[boardik.step]), int(commands[0][1::]) - 1)
            p2 = alphabet.Place(alphabet.num(commands[1][0], langs[boardik.step]), int(commands[1][1::]) - 1)
            p3 = alphabet.Place(alphabet.num(commands[2][0], langs[boardik.step]), int(commands[2][1::]) - 1)
            # Разум заперт изнутри" - Атомное сердце)
            f1 = boardik.figures[boardik.cells[p1.x][p1.y]]
            f2 = boardik.figures[boardik.cells[p2.x][p2.y]]
            f3 = boardik.figures[boardik.cells[p3.x][p3.y]]

            # special cases
            if f1.team != boardik.teams[boardik.step]:
                print("You can't charge with other players' pieces")
                continue
            if f3.team == boardik.teams[boardik.step]:
                print("Do you want to attack your own piece? What a dishonor!")
                continue
            if boardik.cells[p2.x][p2.y] != -1:
                print(f"There is a piece on {commands[1]}. It interrupts my charge!")
                continue

            if (not p2 - p1 in f1.move) or (not f1.can('move', boardik)[p2.x][p2.y] > 0):
                print(f1.name + " can't move there")
                continue  # p1 can't move to place p2
            f1.place = p2

            if (not p3 - p2 in f1.charge) or (not f1.can('charge', boardik)[p3.x][p3.y] > 0):
                print(boardik.figures[boardik.cells[p1.x][p1.y]].name + " can't charge there")
                continue  # p1 can't attack (for now it's = move) to place p2

            # this means that this piece is king
            # if team lose its king, the team is losing
            if f3.name == f3.team.name:
                for i in boardik.teams:
                    if f3.team == i:
                        i.lose = True
                        continue

            boardik.cells[p3.x][p3.y] = -1
            boardik.names[p3.x][p3.y] = "   "
            # Let's not remove prey from figures array (it will be easier to make)

            move(commands[0], commands[1], langs[boardik.step])
            boardik.step = (boardik.step + 1) % len(boardik.teams)
            boardik.print(langs[boardik.step])
        else:
            print("Too many arguments")

    # PRINT COMMAND
    elif first_command == "print":
        boardik.print(langs[boardik.step])

    # HELP COMMAND
    elif first_command == "help":
        print(alphabet.__HELP_MESSAGE__)

    # SKIP COMMAND
    elif first_command == "skip":
        boardik.step = (boardik.step + 1) % len(boardik.teams)
        boardik.print(langs[boardik.step])

    # DEFAULT
    else:
        print("I dont know command " + first_command)
