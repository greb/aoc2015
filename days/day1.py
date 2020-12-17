def solve_part1(inp):
    floor = 0

    for c in inp:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

    return floor


def solve_part2(inp):
    floor = 0

    for i, c in enumerate(inp):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

        if floor == -1:
            return i+1

    assert False
