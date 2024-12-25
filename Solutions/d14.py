class Robot:
    def __init__(self, p, v, m, n):
        self.j, self.i = p
        self.dj, self.di = v
        self.m = m
        self.n = n

    def move(self):
        self.i += self.di
        self.j += self.dj
        if self.j < 0:
            self.j += self.n
        if self.j > self.n - 1:
            self.j -= self.n

        if self.i < 0:
            self.i += self.m
        if self.i > self.m - 1:
            self.i -= self.m


def part1():
    robots = []
    m = 103
    n = 101
    counts = [[0 for _ in range(n)] for _ in range(m)]
    with open("d14.txt") as f:
        for line in f:
            a, b = line.split()
            p = tuple(int(i) for i in a.split("=")[1].split(","))
            v = tuple(int(i) for i in b.split("=")[1].split(","))
            robots.append(Robot(p, v, m, n))
            counts[p[1]][p[0]] += 1

    for i in range(100):
        for robot in robots:
            counts[robot.i][robot.j] -= 1
            robot.move()
            counts[robot.i][robot.j] += 1

    upper_half = counts[: m // 2]
    q1 = [i[: n // 2] for i in upper_half]
    q2 = [i[n // 2 + 1 :] for i in upper_half]
    lower_half = counts[m // 2 + 1 :]
    q3 = [i[: n // 2] for i in lower_half]
    q4 = [i[n // 2 + 1 :] for i in lower_half]

    s1 = sum(sum(i) for i in q1)
    s2 = sum(sum(i) for i in q2)
    s3 = sum(sum(i) for i in q3)
    s4 = sum(sum(i) for i in q4)
    print(f"Part1: {s1 * s2 * s3 * s4}")


def part2():
    robots = []
    m = 103
    n = 101
    counts = [[0 for _ in range(n)] for _ in range(m)]
    with open("d14.txt") as f:
        for line in f:
            a, b = line.split()
            p = tuple(int(i) for i in a.split("=")[1].split(","))
            v = tuple(int(i) for i in b.split("=")[1].split(","))
            robots.append(Robot(p, v, m, n))
            counts[p[1]][p[0]] += 1

    t = 0
    with open("debug.txt", "w") as f:
        # needed to simulate until a christmas tree occurs and look for it in the text file
        while True:
            t += 1
            for robot in robots:
                counts[robot.i][robot.j] -= 1
                robot.move()
                counts[robot.i][robot.j] += 1
            print(f"Time {t}:", file=f)
            print("\n".join("".join("#" if j else "." for j in i) for i in counts), file=f)


if __name__ == "__main__":
    part1()  # 218619120
    part2()  # 7055
