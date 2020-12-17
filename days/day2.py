def needed_paper(dims):
    l, w, h = dims
    sides = [l*w, w*h, h*l]
    slack = min(sides)
    return 2*sum(sides) + slack


def needed_ribbon(dims):
    l, w, h = sorted(dims)
    sides = 2*(l + w)
    volume = l*w*h
    return sides + volume

def solve_part1(inp):
    total = 0

    for line in inp.splitlines():
        dims = [int(d) for d in line.split('x')]
        total += needed_paper(dims)

    return total


def solve_part2(inp):
    total = 0

    for line in inp.splitlines():
        dims = [int(d) for d in line.split('x')]
        total += needed_ribbon(dims)

    return total

