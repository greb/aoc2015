import itertools
import collections

def solve_part1(inp):
    containers = [int(line) for line in inp.splitlines()]

    cnt = 0
    for r in range(2, len(containers)+1):
        for comb in itertools.combinations(containers, r):
            if sum(comb) == 150:
                cnt += 1
    return cnt

def solve_part2(inp):
    containers = [int(line) for line in inp.splitlines()]
    count = collections.defaultdict(int)

    for r in range(2, len(containers)+1):
        for comb in itertools.combinations(containers, r):
            if sum(comb) == 150:
                count[r] += 1

    return count[min(count.keys())]




