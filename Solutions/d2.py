def part1():
    with open("d2.txt") as f:
        out = 0
        for line in f:
            a = list(map(int, line.split()))
            sign = 1 if a[1] - a[0] > 0 else -1
            safe = True
            for i in range(1, len(a)):
                d = a[i] - a[i - 1]
                if sign * d <= 0 or abs(d) < 1 or abs(d) > 3:
                    safe = False
                    break
            if safe:
                out += 1
        print(f"Part1: {out}")


def part2():
    with open("d2.txt") as f:
        out = 0
        for line in f:
            a = list(map(int, line.split()))
            sign = 1 if a[1] - a[0] > 0 else -1
            safe = True
            for i in range(1, len(a)):
                d = a[i] - a[i - 1]
                if sign * d <= 0 or abs(d) < 1 or abs(d) > 3:
                    safe = False

            if safe:
                out += 1
            else:
                for i in range(len(a)):
                    b = [a[j] for j in range(len(a)) if j != i]
                    sign = 1 if b[1] - b[0] > 0 else -1
                    fix = True
                    for i in range(1, len(b)):
                        d = b[i] - b[i - 1]
                        if sign * d <= 0 or abs(d) < 1 or abs(d) > 3:
                            fix = False
                            break
                    if fix:
                        out += 1
                        break
        print(f"Part2: {out}")


if __name__ == "__main__":
    part1()  # 314
    part2()  # 373
