from heapq import heappush, heappop


def part1():
    with open("d16.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    m = len(grid)
    n = len(grid[0])
    goal = (1, n - 2)
    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
    visited = set()
    points = float("inf")
    pq = [(0, m - 2, 1, 0)]
    while pq:
        p, i, j, d = heappop(pq)
        if (i, j) == goal:
            points = min(points, p)
            break
        elif (i, j, d) in visited:
            continue

        visited.add((i, j, d))
        for k in (0, 1, 3):  # no turn, anticlockwise and clockwise
            di, dj = directions[(d + k) % 4]
            i1, j1 = i + di, j + dj
            if i1 in range(m) and j1 in range(n) and grid[i1][j1] != "#":
                extra_point = 1001 if k else 1
                heappush(pq, (p + extra_point, i1, j1, (d + k) % 4))

    print(f"Part1: {points}")


def part2():
    # code is super slow smh
    with open("d16.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    m = len(grid)
    n = len(grid[0])
    seats = set()
    goal = (1, n - 2)
    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
    min_points = [[[float("inf") for _ in range(4)] for j in range(n)] for i in range(m)]
    min_points[m - 2][1] = [0] * 4
    points = float("inf")
    pq = [(0, m - 2, 1, 0, [(m - 2, 1)])]
    while pq:
        p, i, j, d, path = heappop(pq)
        if p > points:
            break
        if (i, j) == goal:
            points = p
            seats.update(path)
            continue
        for k in (0, 1, 3):  # no turn, anticlockwise and clockwise
            di, dj = directions[(d + k) % 4]
            i1, j1 = i + di, j + dj
            if i1 in range(m) and j1 in range(n) and grid[i1][j1] != "#":
                extra_point = 1001 if k else 1
                if p + extra_point <= min_points[i1][j1][(d + k) % 4]:
                    min_points[i1][j1][(d + k) % 4] = p + extra_point
                    heappush(pq, (p + extra_point, i1, j1, (d + k) % 4, path + [(i1, j1)]))

    print(f"Part2: {len(seats)}")


if __name__ == "__main__":
    part1()  # 73432
    part2()  # 496
