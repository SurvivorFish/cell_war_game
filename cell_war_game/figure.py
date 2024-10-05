import BM

class figure:
    name = '   '
    place = []
    moves = []
    team = 'NON'


class guy(figure):
    moves = [(-1, -1), (0, -1), (1, -1)]

    def __init__(self, x, y, team):
        self.name = 'guy'
        self.place = BM.place(x, y)
        self.team = team


class cat(figure):
    def __init__(self, x, y, team):
        self.name = 'cat'
        self.place = BM.place(x, y)
        self.team = team


class king(figure):
    def __init__(self, x, y, team):
        self.name = team.name
        self.place = BM.place(x, y)
        self.team = team
