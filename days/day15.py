import re

def parse(inp):
    ings = []
    for line in inp.splitlines():
        ing = [int(n) for n in re.findall(r'(-?\d+)', line)]
        ings.append(ing)
    return ings

def int_partitions(n, rest):
    if n == 1:
        yield [rest]
        return

    for p in range(0, rest+1):
        for parts in int_partitions(n-1, rest-p):
            yield [p] + parts

def calc_score(ings, part):
    score = 1
    for p in range(4):
        prop = 0
        for a,b in zip(part, [ing[p] for ing in ings]):
            prop += a*b
        if prop < 0:
            return 0
        score *= prop
    return score

def calc_calories(ings, part):
    calories = 0
    for a, b in zip(part, [ing[4] for ing in ings]):
        calories += a*b
    return calories

def solve_part1(inp):
    ings = parse(inp)
    parts = int_partitions(len(ings), 100)
    return max(calc_score(ings, part) for part in parts)

def solve_part2(inp):
    ings = parse(inp)
    parts = int_partitions(len(ings), 100)
    return max(calc_score(ings, part) for part in parts
            if calc_calories(ings, part) == 500)

