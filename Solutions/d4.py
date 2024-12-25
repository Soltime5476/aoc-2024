def part1():
    with open("d4.txt") as f:
        b = [list(line.strip()) for line in f.readlines()]

    m = len(b)
    n = len(b[0])
    paths = 0
    word = "XMAS"
    adj = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
    for i in range(m):
        for j in range(n):
            if b[i][j] != "X":
                continue
            for dr, dc in adj:
                p = 1
                r, c = i, j
                while p < len(word):
                    r, c = r + dr, c + dc
                    if r not in range(m) or c not in range(n):
                        break
                    elif b[r][c] != word[p]:
                        break
                    p += 1
                if p == len(word):
                    paths += 1
    print(f"Part1: {paths}")


def part2():
    with open("d4.txt") as f:
        b = [list(line.strip()) for line in f.readlines()]

    m = len(b)
    n = len(b[0])
    xmas = 0
    for i in range(m):
        for j in range(n):
            if b[i][j] != "A":
                continue
            elif i in (0, m - 1) or j in (0, n - 1):
                continue
            elif b[i - 1][j - 1] + b[i + 1][j + 1] in ("SM", "MS") and b[i + 1][j - 1] + b[i - 1][
                j + 1
            ] in ("SM", "MS"):
                xmas += 1
    print(f"Part2: {xmas}")


if __name__ == "__main__":
    part1()  # 2613
    part2()  # 1905
