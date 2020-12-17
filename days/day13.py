import collections
import itertools

def parse(inp):
    scores = collections.defaultdict(dict)

    for line in inp.splitlines():
        words = line.split()
        person = words[0]
        sign = words[2]
        amount = int(words[3])
        neighbor = words[10][:-1]

        if sign == 'lose':
            amount *= -1

        scores[person][neighbor] = amount

    return scores

def calc_happiness(arrangment, scores):
    pairs = zip(arrangment, arrangment[1:] + (arrangment[0],) )
    happiness = 0
    for a,b in pairs:
        if a == 'me' or b == 'me':
            continue

        happiness += scores[a][b]
        happiness += scores[b][a]
    return happiness

def solve_part1(inp):
    scores = parse(inp)
    arrangments = itertools.permutations(scores.keys())
    return max(calc_happiness(a, scores) for a in arrangments)

def solve_part2(inp):
    scores = parse(inp)

    persons = list(scores.keys())
    persons.append('me')

    arrangments = itertools.permutations(persons)
    return max(calc_happiness(a, scores) for a in arrangments)
