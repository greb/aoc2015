import collections

def parse(inp):
    reindeers = dict()

    for line in inp.splitlines():
        words = line.split()
        reindeer = words[0]
        speed = int(words[3])
        duration = int(words[6])
        pause = int(words[13])

        reindeers[reindeer] = (speed, duration, pause)

    return reindeers


def calc_distance(stats, time):
    speed, duration, pause = stats

    dist = 0
    while time > 0:
        flight_time = min(time, duration)
        dist += speed * flight_time
        time -= duration + pause
    return dist

def solve_part1(inp):
    reindeers = parse(inp)
    time = 2503
    return max(calc_distance(s,time) for s in reindeers.values())


def solve_part2(inp):
    reindeers = parse(inp)
    scores = collections.defaultdict(int)

    for t in range(2503):
        dists = {r: calc_distance(s,t+1) for r,s in reindeers.items()}
        max_dist = max(dists.values())
        for reindeer, dist in dists.items():
            if dist == max_dist:
                scores[reindeer] += 1

    return max(scores.values())
