from collections import Counter


def part1():
    with open("d1.txt") as f:
        a = []
        b = []
        for line in f:
            c, d = map(int, line.split())
            a.append(c)
            b.append(d)
        a.sort()
        b.sort()
        print(f"Part1: {sum(abs(i - j) for i, j in zip(a, b))}")


def part2():
    with open("d1.txt") as f:
        a = []
        b = []
        for line in f:
            c, d = map(int, line.split())
            a.append(c)
            b.append(d)
    c = Counter(b)
    print(f"Part2: {sum(i * c[i] for i in a)}")


if __name__ == "__main__":
    part1()  # 2769675
    part2()  # 24643097
