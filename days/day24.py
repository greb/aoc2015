import itertools

def product(nums):
    prod = 1
    for n in nums:
        prod *= n
    return prod

def distribute(inp, n):
    packages = [int(line) for line in inp.splitlines()]
    target = sum(packages) // n

    for r in itertools.count(2):
        found = []
        for packet in itertools.combinations(packages, r):
            if sum(packet) == target:
                found.append(packet)
        if found:
            break
    return min(product(p) for p in found)


def solve_part1(inp):
    return distribute(inp, 3)

def solve_part2(inp):
    return distribute(inp, 4)


