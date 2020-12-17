import hashlib

def create_hash(key, i):
    secret = key + str(i)
    return hashlib.md5(secret.encode()).hexdigest()

def find_answer(key, n_zeros):
    zeros = '0' * n_zeros
    i = 0
    while True:
        hashed = create_hash(key, i)
        if hashed.startswith(zeros):
            break
        i += 1

    return i

def solve_part1(inp):
    return find_answer(inp.strip(), 5)

def solve_part2(inp):
    return find_answer(inp.strip(), 6)
