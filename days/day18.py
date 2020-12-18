import collections

def parse(inp):
    active = set()
    grid = list(inp.splitlines())
    for y, row in enumerate(grid):
        for x, light in enumerate(row):
            if light == '#':
                active.add((x,y))
    return active

def neighbors(lx,ly):
    for dx in [-1, 0, 1]:
        x = lx + dx
        for dy in [-1, 0, 1]:
            y = ly + dy
            if x==lx and y==ly:
                continue

            if not (0 <= x < 100):
                continue
            if not (0 <= y < 100):
                continue

            yield (x,y)

def evolve(active):
    new_active = set()
    neighbor_count = collections.defaultdict(int)

    for light in active:
        for n in neighbors(*light):
            neighbor_count[n] += 1

    for light, count in neighbor_count.items():
        if light in active:
            if count in [2,3]:
                new_active.add(light)
        else:
            if count == 3:
                new_active.add(light)

    return new_active

def dump(active):
    for y in range(100):
        print(''.join('.#'[(x,y) in active] for x in range(100)))
    print()


def solve_part1(inp):
    active = parse(inp)

    for _ in range(100):
        active = evolve(active)

    return len(active)

def stuck(active):
    active.add((0,0))
    active.add((0,99))
    active.add((99,0))
    active.add((99,99))

def solve_part2(inp):
    active = parse(inp)
    stuck(active)
    dump(active)
    for _ in range(100):
        active = evolve(active)
        stuck(active)
        dump(active)

    return len(active)
