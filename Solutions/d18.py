from collections import deque


def part1():
    m = 70
    n = 70
    sim = 1024
    mem = [["." for j in range(m + 1)] for i in range(n + 1)]
    with open("d18.txt") as f:
        for _ in range(sim):
            line = f.readline().strip()
            y, x = map(int, line.split(","))
            mem[x][y] = "#"

    adj = ((1, 0), (0, 1), (-1, 0), (0, -1))
    q = deque()
    visited = set()
    q.append((0, 0))
    visited.add((0, 0))
    dist = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) == (m, n):
                print(f"Part1: {dist}")
            for di, dj in adj:
                r, c = i + di, j + dj
                if (
                    r in range(m + 1)
                    and c in range(n + 1)
                    and mem[r][c] == "."
                    and (r, c) not in visited
                ):
                    visited.add((r, c))
                    q.append((r, c))
        dist += 1


def part2():
    m = 70
    n = 70
    sim = 1024
    mem = [["." for j in range(m + 1)] for i in range(n + 1)]
    adj = ((1, 0), (0, 1), (-1, 0), (0, -1))

    with open("d18.txt") as f:
        for _ in range(sim):
            line = f.readline().strip()
            y, x = map(int, line.split(","))
            mem[x][y] = "#"

        a = sim
        # may look for other solutions than brute force
        for line in f:
            a += 1
            y, x = map(int, line.split(","))
            mem[x][y] = "#"
            q = deque()
            visited = set()
            q.append((0, 0))
            visited.add((0, 0))
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for di, dj in adj:
                        r, c = i + di, j + dj
                        if (
                            r in range(m + 1)
                            and c in range(n + 1)
                            and mem[r][c] == "."
                            and (r, c) not in visited
                        ):
                            visited.add((r, c))
                            q.append((r, c))
                if (m, n) in visited:
                    break

            if (m, n) not in visited:
                print(f"Part2: {y},{x}")
                break


if __name__ == "__main__":
    part1() # 360
    part2() # 58,62
