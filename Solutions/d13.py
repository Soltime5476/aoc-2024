import scipy.linalg as linalg
import scipy.special


def part1():
    tokens = 0
    with open("d13.txt") as f:
        while f:
            A = f.readline()
            if not A:
                break
            B = f.readline()
            prize = f.readline()
            f.readline()

            a, c = (int(exp.split("+")[1]) for exp in A.split(": ")[1].split(", "))
            b, d = (int(exp.split("+")[1]) for exp in B.split(": ")[1].split(", "))
            m, n = (int(exp.split("=")[1]) for exp in prize.split(": ")[1].split(", "))
            A = [[a, b], [c, d]]

            x, y = linalg.solve(A, (m, n))
            if x < 0 or y < 0 or x > 100 or y > 100:
                continue

            x = scipy.special.round(x)
            y = scipy.special.round(y)
            if a * x + b * y == m and c * x + d * y == n:
                tokens += 3 * x + y

        print(f"Part1: {tokens}")


def part2():
    tokens = 0
    with open("d13.txt") as f:
        while f:
            A = f.readline()
            if not A:
                break
            B = f.readline()
            prize = f.readline()
            f.readline()

            a, c = (int(exp.split("+")[1]) for exp in A.split(": ")[1].split(", "))
            b, d = (int(exp.split("+")[1]) for exp in B.split(": ")[1].split(", "))
            m, n = (
                10000000000000 + int(exp.split("=")[1]) for exp in prize.split(": ")[1].split(", ")
            )
            A = [[a, b], [c, d]]

            x, y = linalg.solve(A, (m, n))
            if x < 0 or y < 0:
                continue

            x = scipy.special.round(x)
            y = scipy.special.round(y)
            if a * x + b * y == m and c * x + d * y == n:
                tokens += 3 * x + y

        print(f"Part2: {tokens}")


if __name__ == "__main__":
    part1()  # 37297
    part2()  # 83197086729371
