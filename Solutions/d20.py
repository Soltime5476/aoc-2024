def part1():
    with open("d20.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    path = {}
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                start = i, j
            elif grid[i][j] == "E":
                end = i, j
            elif grid[i][j] == ".":
                path[(i, j)] = float("inf")

    adj = ((0, -1), (1, 0), (0, 1), (-1, 0))
    adj_2 = set()
    for i in range(2, 3):
        for j in range(i + 1):
            adj_2.add((j, i - j))
            adj_2.add((-j, i - j))
            adj_2.add((-j, j - i))
            adj_2.add((j, j - i))
    path[start] = 0
    path[end] = float("inf")

    q = start
    p = 0
    while q:
        if q == end:
            break
        i, j = q
        for di, dj in adj:
            i1, j1 = i + di, j + dj
            if (
                i1 in range(m)
                and j1 in range(n)
                and grid[i1][j1] != "#"
                and path[(i1, j1)] == float("inf")
            ):
                path[(i1, j1)] = p + 1
                q = i1, j1
        p += 1

    total = 0
    for i, j in path.items():
        r, c = i
        for dr, dc in adj_2:
            r1, c1 = r + dr, c + dc
            if (r1, c1) not in path:
                continue
            if j - (path[(r1, c1)] + abs(dr) + abs(dc)) >= 100:
                total += 1

    print(f"Part1: {total}")


def part2():
    with open("d20.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    path = {}
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                start = i, j
            elif grid[i][j] == "E":
                end = i, j
            elif grid[i][j] == ".":
                path[(i, j)] = float("inf")

    adj = ((0, -1), (1, 0), (0, 1), (-1, 0))
    adj_20 = set()
    for i in range(2, 21):
        for j in range(i + 1):
            adj_20.add((j, i - j))
            adj_20.add((-j, i - j))
            adj_20.add((-j, j - i))
            adj_20.add((j, j - i))
    path[start] = 0
    path[end] = float("inf")

    q = start
    p = 0
    while q:
        if q == end:
            break
        i, j = q
        for di, dj in adj:
            i1, j1 = i + di, j + dj
            if (
                i1 in range(m)
                and j1 in range(n)
                and grid[i1][j1] != "#"
                and path[(i1, j1)] == float("inf")
            ):
                path[(i1, j1)] = p + 1
                q = i1, j1
        p += 1

    total = 0
    for i, j in path.items():
        r, c = i
        for dr, dc in adj_20:
            r1, c1 = r + dr, c + dc
            if (r1, c1) not in path:
                continue
            if j - (path[(r1, c1)] + abs(dr) + abs(dc)) >= 100:
                total += 1

    print(f"Part2: {total}")


if __name__ == "__main__":
    part1()  # 1530
    part2()  # 1033983
