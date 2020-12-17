directions = {
    '^': (0, -1),
    'v': (0, 1),
    '>': (1, 0),
    '<': (-1, 0)
}

def move_position(pos, move):
    return tuple(p+d for p,d in zip(pos, directions[move]))

def solve_part1(inp):
    pos = (0,0)
    houses = set([pos])

    for move in inp:
        pos = move_position(pos, move)
        houses.add(pos)

    return len(houses)

def solve_part2(inp):
    santa = (0,0)
    robot = (0,0)
    santa_houses = set([santa])
    robot_houses = set([robot])

    for i, move in enumerate(inp):
        if i % 2 == 0:
            santa = move_position(santa, move)
            santa_houses.add(santa)
        else:
            robot = move_position(robot, move)
            robot_houses.add(robot)

    return len(santa_houses | robot_houses)
