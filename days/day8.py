def count_unescape(s):
    cnt = 0
    idx = 1

    while idx < len(s)-1:
        if s[idx] == '\\':
            n = s[idx+1]
            if n == 'x':
                idx += 4
            else:
                idx += 2
        else:
            idx += 1
        cnt += 1
    return cnt

def count_escape(s):
    cnt = 0
    for c in s:
        if c in '\\"':
            cnt += 2
        else:
            cnt += 1
    return cnt + 2

def solve_part1(inp):
    total_code = 0
    total_chars = 0
    for line in inp.splitlines():
        total_code += len(line)
        total_chars += count_unescape(line)

    return total_code - total_chars

def solve_part2(inp):
    total_code = 0
    total_chars = 0
    for line in inp.splitlines():
        total_code += len(line)
        total_chars += count_escape(line)

    return total_chars - total_code
