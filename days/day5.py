import re

def solve_part1(inp):
    cnt = 0
    for line in inp.splitlines():
        vowels = re.findall(r'[aeoiu]', line)
        if len(vowels) < 3:
            continue

        doubles = re.findall(r'(.)\1', line)
        if len(doubles) < 1:
            continue

        forbidden = re.findall(r'ab|cd|pq|xy', line)
        if len(forbidden) > 0:
            continue

        cnt += 1

    return cnt


def solve_part2(inp):
    cnt = 0
    for line in inp.splitlines():
        pairs = re.findall(r'(..).*\1', line)
        if len(pairs) < 1:
            continue

        repeat = re.findall(r'(.).\1', line)
        if len(repeat) < 1:
            continue

        cnt += 1

    return cnt
