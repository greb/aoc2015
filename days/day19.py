import re
import itertools

def parse(inp):
    rules = []
    lines = inp.splitlines()
    for line in lines:
        if not line:
            break
        rules.append(line.split(' => '))
    return lines[-1], rules

def gen_mols(mol, src, dst):
    spans = (m.span() for m in  re.finditer(src, mol))
    for a,b in spans:
        start = mol[:a]
        end   = mol[b:]
        yield start + dst + end

def solve_part1(inp):
    mol, rules = parse(inp)

    mols = set()
    for src, dst in rules:
        mols.update(gen_mols(mol, src, dst))
    return len(mols)

def solve_part2(inp):
    mol, rules = parse(inp)

    cnt = 0
    while mol != 'e':
        for src, dst in rules:
            if dst in mol:
                mol = mol.replace(dst, src, 1)
                cnt += 1
                break
    return cnt



