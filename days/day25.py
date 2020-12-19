import re

def gen_coords():
    row = 1
    x, y = 1, row

    while True:
        while y > 0:
            yield (x,y)
            x += 1
            y -= 1
        row += 1
        x, y = 1, row

def gen_values():
    c = 20151125
    m = 252533
    d = 33554393

    while True:
        yield c
        c = (c*m) % d

def solve_part1(inp):
    row, col = (int(n) for n in re.findall(r'\d+', inp))

    for (x,y),v in zip(gen_coords(), gen_values()):
        if x == col and y == row:
            return v



