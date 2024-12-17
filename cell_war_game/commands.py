from abc import ABC, abstractmethod

from board import Board


class Command(ABC):
    @abstractmethod
    def filter(self, args: list[str]) -> bool:
        pass
    
    @abstractmethod
    def action(self, board: Board):
        pass
    

class HelpCommand(Command):
    def filter(self, args: list[str]) -> bool:
        return len(args) == 1 and args[0] == 'help'
    
    def action(self, _: Board):
        print('Help message....')
        

class PrintCommand(Command):
    def __init__(self, langs: list[str]):
        super().__init__()
        self.langs = langs
    
    def filter(self, args: list[str]) -> bool:
        return len(args) == 1 and args[0] == 'print'
    
    def action(self, board: Board):
        board.print(self.langs[board.step])
        


'''
Main тогда может выглядеть вот так:
'''

board: Board = None
langs = import_langs(board.teams)

_ALL_COMMANDS: list[Command] = [
    HelpCommand(),
    PrintCommand(langs)
]


while True:
    args = input().strip().split()
    for command in _ALL_COMMANDS:
        if command.filter(args):
            command.action(board)
            continue