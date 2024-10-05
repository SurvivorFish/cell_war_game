class figure:
    name = '   '
    place = []


class guy(figure):
    def __init__(self, x, y):
        self.name = 'guy'
        self.place = [x, y]

class cat(figure):
    def __init__(self, x, y):
        self.name = 'cat'
        self.place = [x, y]