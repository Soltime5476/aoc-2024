from collections import deque


def bfs(grid, i, j, visited):
    m = len(grid)
    n = len(grid[0])
    adj = ((1, 0), (-1, 0), (0, 1), (0, -1))
    q = deque([(i, j)])
    visited.add((i, j))
    area = 0
    peri = 0
    while q:
        r, c = q.popleft()
        area += 1
        for dr, dc in adj:
            r1, c1 = r + dr, c + dc
            if r1 in range(m) and c1 in range(n) and grid[r1][c1] == grid[r][c]:
                if (r1, c1) not in visited:
                    visited.add((r1, c1))
                    q.append((r1, c1))
            else:
                peri += 1
    return area, peri


def part1():
    with open("d12.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    m = len(grid)
    n = len(grid[0])
    visited = set()
    cost = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                area, peri = bfs(grid, i, j, visited)
                cost += area * peri

    print(f"Part1: {cost}")


def bfs_p2(grid, i, j, visited):
    visited.add((i, j))
    q = deque([(i, j)])
    area = 0
    corners = 0
    m = len(grid)
    n = len(grid[0])
    adj = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while q:
        r, c = q.popleft()
        area += 1
        v = grid[r][c]
        N = grid[r - 1][c] if r - 1 in range(m) else ""
        S = grid[r + 1][c] if r + 1 in range(m) else ""
        W = grid[r][c - 1] if c - 1 in range(n) else ""
        E = grid[r][c + 1] if c + 1 in range(n) else ""
        NE = grid[r - 1][c + 1] if r - 1 in range(m) and c + 1 in range(n) else ""
        SE = grid[r + 1][c + 1] if r + 1 in range(m) and c + 1 in range(n) else ""
        SW = grid[r + 1][c - 1] if r + 1 in range(m) and c - 1 in range(n) else ""
        NW = grid[r - 1][c - 1] if r - 1 in range(m) and c - 1 in range(n) else ""

        if v not in (N, E):
            corners += 1
        if NE != v and N == v and E == v:
            corners += 1

        if v not in (S, E):
            corners += 1
        if SE != v and S == v and E == v:
            corners += 1

        if v not in (S, W):
            corners += 1
        if SW != v and S == v and W == v:
            corners += 1

        if v not in (N, W):
            corners += 1
        if NW != v and N == v and W == v:
            corners += 1

        for dr, dc in adj:
            r1, c1 = r + dr, c + dc
            if r1 in range(m) and c1 in range(n) and grid[r1][c1] == grid[r][c]:
                if (r1, c1) not in visited:
                    visited.add((r1, c1))
                    q.append((r1, c1))

    return area, corners


def part2():
    with open("d12.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    m = len(grid)
    n = len(grid[0])
    visited = set()
    cost = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                area, sides = bfs_p2(grid, i, j, visited)
                cost += area * sides
    print(f"Part2: {cost}")


if __name__ == "__main__":
    part1()  # 1361494
    part2()  # 830516
