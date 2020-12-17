import itertools

def look_and_say(s):
    say = ''
    for n, g in itertools.groupby(s):
        l = len(list(g))
        say += str(l) + n
    return say

def solve_part1(inp):
    s = inp.strip()
    for _ in range(40):
        s = look_and_say(s)

    return len(s)

def solve_part2(inp):
    s = inp.strip()
    for _ in range(50):
        s = look_and_say(s)

    return len(s)
