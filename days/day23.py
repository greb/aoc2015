import re

class Computer:
    def __init__(self, code):
        self.pc = 0
        self.reg_a = 0
        self.reg_b = 0
        self.code = code

    def load_reg(self, r):
        if r == 'a':
            return self.reg_a
        elif r == 'b':
            return self.reg_b

    def store_reg(self, r, val):
        if r == 'a':
            self.reg_a = val
        elif r == 'b':
            self.reg_b = val

    def step(self):
        instr = self.code[self.pc]

        if m := re.fullmatch(r'([a-z]*) (.)', instr):
            op, r = m.groups()
            val = self.load_reg(r)
            if op == 'hlf':
                val //= 2
            elif op == 'tpl':
                val *= 3
            elif op == 'inc':
                val += 1
            self.store_reg(r, val)
            self.pc += 1

        elif m := re.fullmatch(r'([a-z]*) ([\+-]\d*)', instr):
            op, offset = m.groups()
            self.pc += int(offset)

        elif m := re.fullmatch(r'([a-z]*) ([ab]), ([\+-]\d*)', instr):
            op, r, offset = m.groups()
            val = self.load_reg(r)
            if op == 'jie':
                if val % 2 == 0:
                    self.pc += int(offset)
                else:
                    self.pc += 1
            elif op == 'jio':
                if val == 1:
                    self.pc += int(offset)
                else:
                    self.pc += 1

def solve_part1(inp):
    c = Computer(inp.splitlines())

    while c.pc < len(c.code):
        c.step()

    return c.load_reg('b')


def solve_part2(inp):
    c = Computer(inp.splitlines())
    c.reg_a = 1

    while c.pc < len(c.code):
        c.step()

    return c.load_reg('b')
