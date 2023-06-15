G = 10

def make_closure():
    a = 1
    b = 2
    def inner(x):
        return x + G + a
    return inner