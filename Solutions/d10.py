from collections import deque


def part1():
    with open("d10.txt") as f:
        grid = [list(int(i) for i in line.strip()) for line in f.readlines()]

    m = len(grid)
    n = len(grid[0])
    adj = ((0, 1), (1, 0), (-1, 0), (0, -1))
    dep = [[0 for j in range(n)] for i in range(m)]

    src = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 9]
    q = deque()
    for s in src:
        q.append(s)
        visited = set()
        while q:
            i, j = q.popleft()
            dep[i][j] += 1
            for dr, dc in adj:
                r, c = i + dr, j + dc
                if (
                    r in range(m)
                    and c in range(n)
                    and grid[r][c] == grid[i][j] - 1
                    and (r, c) not in visited
                ):
                    q.append((r, c))
                    visited.add((r, c))

    print(f"Part1: {sum(dep[i][j] for i in range(m) for j in range(n) if grid[i][j] == 0)}")


def part2():
    with open("d10.txt") as f:
        grid = [list(int(i) for i in line.strip()) for line in f.readlines()]

    m = len(grid)
    n = len(grid[0])
    adj = ((0, 1), (1, 0), (-1, 0), (0, -1))
    dep = [[grid[i][j] == 9 for j in range(n)] for i in range(m)]
    q = deque((i, j) for i in range(m) for j in range(n) if grid[i][j] == 9)
    visited = set()
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for dr, dc in adj:
                r, c = i + dr, j + dc
                if r not in range(m) or c not in range(n) or grid[r][c] != grid[i][j] - 1:
                    continue
                dep[r][c] += dep[i][j]
                if (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))

    print(f"Part2: {sum(dep[i][j] for i in range(m) for j in range(n) if grid[i][j] == 0)}")


if __name__ == "__main__":
    part1()  # 574
    part2()  # 1238
