import re
import itertools

weapons = [
    [8,4,0], [10,5,0], [25,6,0], [40,7,0], [74,8,0]
]

armors = [
    [0,0,0], [13,0,1], [31,0,2], [53,0,3], [75,0,4], [102,0,5]
]

rings = [
    [0,0,0], [0,0,0], [25,1,0], [50,2,0], [100,3,0], [20,0,1], [40,0,2],
    [80,0,3]
]

def gen_equipment():
    for weapon in weapons:
        for armor in armors:
            for ring1, ring2 in itertools.combinations(rings, 2):
                yield [sum(p) for p in zip(weapon, armor, ring1, ring2)]

def parse(inp):
    return [int(n) for n in re.findall(r'\d+', inp)]


def player_wins(player, boss):
    player_hp = player[0]
    boss_hp = boss[0]

    player_dam = max(player[1] - boss[2], 0)
    boss_dam   = max(boss[1] - player[2], 0)

    while True:
        boss_hp -= player_dam
        if boss_hp <= 0:
            return True

        player_hp -= boss_dam
        if player_hp <= 0:
            return False

def solve_part1(inp):
    boss = parse(inp)
    hp = 100

    costs = []
    for cost, dam, arm in gen_equipment():
        player = hp, dam, arm
        if player_wins(player, boss):
            costs.append(cost)

    return min(costs)

def solve_part2(inp):
    boss = parse(inp)
    hp = 100

    costs = []
    for cost, dam, arm in gen_equipment():
        player = hp, dam, arm
        if not player_wins(player, boss):
            costs.append(cost)

    return max(costs)
