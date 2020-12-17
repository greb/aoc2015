size = 1000

def parse(inp):
    instrs = []
    parse_pos = lambda w: tuple(int(n) for n in w.split(','))

    for line in inp.splitlines():
        words = line.split()
        if words[0] == 'turn':
            instr = words[1]
        else:
            instr = words[0]
        start = parse_pos(words[-3])
        end = parse_pos(words[-1])

        instrs.append( (instr, start, end) )

    return instrs

def make_grid():
    return [[0 for _ in range(size)] for _ in range(size)]

def instr_part1(grid, instr):
    instr, start, end = instr

    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            if instr == 'toggle':
                grid[x][y] = not grid[x][y]
            elif instr == 'on':
                grid[x][y] = True
            elif instr == 'off':
                grid[x][y] = False

def instr_part2(grid, instr):
    instr, start, end = instr

    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            if instr == 'toggle':
                grid[x][y] += 2
            elif instr == 'on':
                grid[x][y] += 1
            elif instr == 'off':
                if grid[x][y] > 0:
                    grid[x][y] -= 1


def count_lights(grid):
    return sum(light for line in grid for light in line)

def solve_part1(inp):
    instrs = parse(inp)
    grid = make_grid()

    for instr in instrs:
        instr_part1(grid, instr)
    return count_lights(grid)

def solve_part2(inp):
    instrs = parse(inp)
    grid = make_grid()

    for instr in instrs:
        instr_part2(grid, instr)
    return count_lights(grid)
