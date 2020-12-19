import re
import collections
import itertools

spell_costs = {
    'missile':  53,
    'drain':    73,
    'shield':   113,
    'poison':   173,
    'recharge': 229
}

def parse(inp):
    return [int(n) for n in re.findall(r'\d+', inp)]

class Fight:
    def __init__(self, boss, spells):
        self.boss_hp, self.boss_dam = boss
        self.spells = spells

        self.player_hp = 50
        self.player_arm = 0
        self.player_mana = 500

        self.effects = collections.defaultdict(int)

    def cast_spell(self):
        if not self.spells:
            return False

        spell = self.spells[0]
        self.spells = self.spells[1:]

        cost = spell_costs[spell]
        self.player_mana -= cost
        if self.player_mana < 0:
            return False 

        if spell == 'missile':
            self.boss_hp -= 4
        elif spell == 'drain':
            self.boss_hp -= 2
            self.player_hp += 2
        else:
            if self.effects[spell] > 0:
                return False

            if spell == 'shield':
                self.player_arm = 7
                self.effects[spell] = 6
            elif spell == 'poison':
                self.effects[spell] = 6
            elif spell == 'recharge':
                self.effects[spell] = 5

        return True

    def deal_effects(self):
        for effect in self.effects:
            timer = self.effects[effect]
            if timer > 0:
                if effect == 'poison':
                    self.boss_hp -= 3
                elif effect == 'recharge':
                    self.player_mana += 101

                self.effects[effect] -= 1
            else:
                if effect == 'shield':
                    self.player_arm = 0

    def fight(self, hard=False):
        player_turn = True

        while True:
            if hard and player_turn:
                self.player_hp -= 1
                if self.player_hp <= 0:
                    return False

            self.deal_effects()
            if self.boss_hp <= 0:
                # Boss might die because of effects
                return True

            if player_turn:
                success = self.cast_spell()
                if not success:
                    return False
                if self.boss_hp <= 0:
                    return True

            else:
                dam = max(self.boss_dam - self.player_arm, 1)
                self.player_hp -= dam
                if self.player_hp <= 0:
                    return False

            player_turn = not player_turn


def find_score(boss, hard=False):
    for r in itertools.count(2):
        found_scores = []

        for spells in itertools.product(spell_costs.keys(), repeat=r):
            if Fight(boss, spells).fight(hard):
                s = sum(spell_costs[s] for s in spells)
                print(f'with {s} -> {spells}')
                found_scores.append(s)
        if found_scores:
            return min(found_scores)


def solve_part1(inp):
    boss = parse(inp)
    return find_score(boss, False)

def solve_part2(inp):
    boss = parse(inp)
    return find_score(boss, True)
