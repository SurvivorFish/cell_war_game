class C:
    lst: list

    def __init__(self, lst: list):
        self.lst = lst


def test(c: C):
    c.lst.pop()
    return


c = C([1,2,3])
test(c)
print(c.lst)
