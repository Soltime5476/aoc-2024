from itertools import product
from functools import cache


def find_presses(code, depth):
    paths = {
        "A": {
            "A": ["A"],
            "^": ["<A"],
            "v": ["<vA", "v<A"],
            ">": ["vA"],
            "<": ["v<<A"],
        },
        "^": {
            "A": [">A"],
            "^": ["A"],
            "v": ["vA"],
            ">": ["v>A", ">vA"],
            "<": ["v<A"],
        },
        "v": {
            "A": ["^>A", ">^A"],
            "^": ["^A"],
            "v": ["A"],
            ">": [">A"],
            "<": ["<A"],
        },
        "<": {
            "A": [">>^A"],
            "^": [">^A"],
            "v": [">A"],
            ">": [">>A"],
            "<": ["A"],
        },
        ">": {
            "A": ["^A"],
            "^": ["<^A", "^<A"],
            "v": ["<A"],
            ">": ["A"],
            "<": ["<<A"],
        },
    }

    @cache
    def cost(s, depth):
        if depth == 0:
            return len(s)
        elif s == "A":
            return 1

        ret = 0
        last = "A"
        for i in s:
            ret += min(cost(path, depth - 1) for path in paths[last][i])
            last = i
        return ret

    presses = cost(code, depth)
    return presses


def part1():
    with open("d21.txt") as f:
        codes = tuple(line.strip() for line in f.readlines())

    pos = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "0": (3, 1),
        "A": (3, 2),
    }

    start = "A"
    complexity = 0
    for code in codes:
        trials = []
        for c in code:
            r1, c1 = pos[start]
            r2, c2 = pos[c]
            dr, dc = r2 - r1, c2 - c1
            if dr < 0:
                s1 = "^" * abs(dr)
            else:
                s1 = "v" * dr
            if dc < 0:
                s2 = "<" * abs(dc)
            else:
                s2 = ">" * dc

            possible = [s1 + s2]
            if s1 and s2 and (r1, c1 + dc) != (3, 0):
                possible.append(s2 + s1)
            trials.append(possible)
            start = c

        p = float("inf")
        for i in product(*trials):
            path = "A".join(i) + "A"
            p = min(p, find_presses(path, 2))

        complexity += int(code[:-1]) * p

    print(f"Part1: {complexity}")


def part2():
    with open("d21.txt") as f:
        codes = tuple(line.strip() for line in f.readlines())

    pos = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "0": (3, 1),
        "A": (3, 2),
    }

    start = "A"
    complexity = 0
    for code in codes:
        trials = []
        for c in code:
            r1, c1 = pos[start]
            r2, c2 = pos[c]
            dr, dc = r2 - r1, c2 - c1
            if dr < 0:
                s1 = "^" * abs(dr)
            else:
                s1 = "v" * dr
            if dc < 0:
                s2 = "<" * abs(dc)
            else:
                s2 = ">" * dc

            possible = [s1 + s2]
            if s1 and s2 and (r1, c1 + dc) != (3, 0):
                possible.append(s2 + s1)
            trials.append(possible)
            start = c

        p = float("inf")
        for i in product(*trials):
            path = "A".join(i) + "A"
            p = min(p, find_presses(path, 25))

        complexity += int(code[:-1]) * p

    print(f"Part2: {complexity}")


if __name__ == "__main__":
    part1()  # 248108
    part2()  # 303836969158972
