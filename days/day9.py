import itertools
import collections

def parse(inp):
    dists = collections.defaultdict(dict)

    for line in inp.splitlines():
        words = line.split()
        a = words[0]
        b = words[2]
        dist = int(words[4])

        dists[a][b] = dist
        dists[b][a] = dist
    return dists

def calc_dist(route, dists):
    return sum(dists[a][b] for a,b in zip(route, route[1:]))

def solve_part1(inp):
    dists = parse(inp)
    routes = itertools.permutations(dists.keys())
    return min(calc_dist(r, dists) for r in routes)

def solve_part2(inp):
    dists = parse(inp)
    routes = itertools.permutations(dists.keys())
    return max(calc_dist(r, dists) for r in routes)
