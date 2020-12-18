def solve_part1(inp):
    n_presents = int(inp.strip()) // 10

    houses = [0] * n_presents
    for e in range(1, n_presents):
        for h in range(e, n_presents, e):
            houses[h] += e

    for i, h in enumerate(houses):
        if h > n_presents:
            return i

def solve_part2(inp):
    n_presents = int(inp.strip())

    houses = [0] * n_presents
    for e in range(1, n_presents // 10):
        for i in range(50):
            idx = e+i*e
            if idx >= n_presents:
                break
            houses[idx] += 11 * e

    for i, h in enumerate(houses):
        if h > n_presents:
            return i
