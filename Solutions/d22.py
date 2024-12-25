from collections import defaultdict, deque


def part1():
    s = 0
    prune = (1 << 24) - 1  # 16777216 = 2^24 - 1
    with open("d22.txt") as f:
        secrets = [int(line.strip()) for line in f.readlines()]
    for secret in secrets:
        for _ in range(2000):
            secret = (secret ^ (secret << 6)) & prune
            secret = (secret ^ (secret >> 5)) & prune
            secret = (secret ^ (secret << 11)) & prune
        s += secret

    print(f"Part1: {s}")


def part2():
    with open("d22.txt") as f:
        secrets = [int(line.strip()) for line in f.readlines()]

    prune = (1 << 24) - 1
    best = defaultdict(int)
    for secret in secrets:
        q = deque(maxlen=4)
        visited = set()
        for _ in range(2000):
            old_secret = secret
            secret = (secret ^ (secret << 6)) & prune
            secret = (secret ^ (secret >> 5)) & prune
            secret = (secret ^ (secret << 11)) & prune
            q.append(secret % 10 - old_secret % 10)
            t = tuple(q)
            if len(q) == 4 and t not in visited:
                visited.add(t)
                best[t] += secret % 10

    print(f"Part2: {max(best.values())}")


if __name__ == "__main__":
    part1() # 14869099597
    part2() # 1717
