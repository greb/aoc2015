import re

def parse(inp):
    sues = []
    for line in inp.splitlines():
        line = line[line.find(':')+1:]
        vals = re.findall(r'([a-z]*): (\d*)', line)
        sues.append({i: int(a) for i,a in vals})
    return sues


target = {
    'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
    'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2,
    'perfumes': 1
}


def solve_part1(inp):
    sues = parse(inp)
    for sue, stuff in enumerate(sues):
        cnt = 0
        for item, amount in stuff.items():
            if amount == target[item]:
                cnt += 1

        if cnt == len(stuff):
            return sue+1


def solve_part2(inp):
    sues = parse(inp)
    for sue, stuff in enumerate(sues):
        cnt = 0
        for item, amount in stuff.items():
            if item in ['cats', 'trees']:
                if amount > target[item]:
                    cnt += 1
            elif item in ['pomeranians', 'goldfish']:
                if amount < target[item]:
                    cnt += 1
            elif amount == target[item]:
                cnt += 1

        if cnt == len(stuff):
            return sue+1
