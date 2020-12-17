import itertools

forbidden = set(ord(c)-97 for c in 'iol')

def decode_b26(s):
    digits = []
    for c in s:
        digits.append(ord(c) - 97)
    return digits

def incr_b26(digits):
    of = True
    idx = len(digits) - 1
    while of and idx > 0:
        of, d = divmod(digits[idx]+1, 26)
        digits[idx] = d
        idx -= 1

def encode_b64(digits):
    s = ''
    for d in digits:
        s += chr(d + 97)
    return s

def check_incr(digits):
    for a,b,c in zip(digits, digits[1:], digits[2:]):
        if c-b == 1 and b-a == 1:
            return True
    return False

def check_forbidden(digits):
    return all(d not in forbidden for d in digits)

def check_pairs(digits):
    pairs = set()
    for n, g in itertools.groupby(digits):
        if len(list(g)) == 2:
            pairs.add(n)
    return len(pairs) >= 2

def next_pw(pw):
    pw = decode_b26(pw)
    while True:
        incr_b26(pw)
        if check_incr(pw) and check_forbidden(pw) and check_pairs(pw):
            break

    return encode_b64(pw)

def solve_part1(inp):
    s = inp.strip()
    return next_pw(s)

def solve_part2(inp):
    s = inp.strip()
    s = next_pw(s)
    return next_pw(s)
