def parse(inp):
    circuit = {}
    for line in inp.splitlines():
        rule, wire = line.split(' -> ')
        circuit[wire] = rule.split()
    return circuit


def find_value(node, circuit, wires):
    if node.isdigit():
        return int(node)

    if node in wires:
        return wires[node]

    rule = circuit[node]
    if len(rule) == 1:
        wire = find_value(rule[0], circuit, wires)
    else:
        gate = rule[-2]
        if gate == 'NOT':
            op1 = find_value(rule[1], circuit, wires)
            wire = 0xffff ^ op1
        else:
            op1 = find_value(rule[0], circuit, wires)
            op2 = find_value(rule[2], circuit, wires)

            if gate == 'AND':
                wire = op1 & op2
            elif gate == 'OR':
                wire = op1 | op2
            elif gate == 'RSHIFT':
                wire = op1 >> op2
            elif gate == 'LSHIFT':
                wire = op1 << op2

    wires[node] = wire
    return wire


def solve_part1(inp):
    circuit = parse(inp)
    wires = dict()
    return find_value('a', circuit, wires)

def solve_part2(inp):
    circuit = parse(inp)

    wires = dict()
    a_val = find_value('a', circuit, wires)

    wires = {'b': a_val}
    return find_value('a', circuit, wires)
