import json

def sum_json(obj, part2=False):
    if isinstance(obj, int):
        return obj
    s = 0
    if isinstance(obj, dict):
        for value in obj.values():
            if part2 and value == 'red':
                return 0
            s += sum_json(value, part2)
    elif isinstance(obj, list):
        for value in obj:
            s += sum_json(value, part2)
    return s

def solve_part1(inp):
    doc = json.loads(inp)
    return sum_json(doc)

def solve_part2(inp):
    doc = json.loads(inp)
    return sum_json(doc, part2=True)
