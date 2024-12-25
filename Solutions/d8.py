from collections import defaultdict
from itertools import combinations


def part1():
    with open("d8.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    m = len(grid)
    n = len(grid[0])
    antennas = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if grid[i][j] != ".":
                antennas[grid[i][j]].append((i, j))

    antinodes = set()
    for a in antennas.values():
        for (i1, j1), (i2, j2) in combinations(a, r=2):
            di = i2 - i1
            dj = j2 - j1
            if i1 - di in range(m) and j1 - dj in range(n):
                antinodes.add((i1 - di, j1 - dj))
            if i2 + di in range(m) and j2 + dj in range(n):
                antinodes.add((i2 + di, j2 + dj))

    print(f"Part1: {len(antinodes)}")


def part2():
    with open("d8.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    m = len(grid)
    n = len(grid[0])
    antennas = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if grid[i][j] != ".":
                antennas[grid[i][j]].append((i, j))

    antinodes = set()
    for a in antennas.values():
        for (i1, j1), (i2, j2) in combinations(a, r=2):
            antinodes.add((i1, j1))
            antinodes.add((i2, j2))
            di = i2 - i1
            dj = j2 - j1
            while i1 - di in range(m) and j1 - dj in range(n):
                antinodes.add((i1 - di, j1 - dj))
                i1 -= di
                j1 -= dj

            while i2 + di in range(m) and j2 + dj in range(n):
                antinodes.add((i2 + di, j2 + dj))
                i2 += di
                j2 += dj

    print(f"Part2: {len(antinodes)}")


if __name__ == "__main__":
    part1()  # 423
    part2()  # 1287
