from itertools import cycle


def part1():
    with open("d6.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    m, n = len(grid), len(grid[0])
    r, c = None, None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "^":
                r, c = i, j
                break

    grid[r][c] = "X"
    directions = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))
    for dr, dc in directions:
        if r not in range(m) or c not in range(n):
            break
        while True:
            r += dr
            c += dc
            if r in range(m) and c in range(n):
                if grid[r][c] != "#":
                    grid[r][c] = "X"
                else:
                    r -= dr
                    c -= dc
                    break
            else:
                break

    print(f"Part1: {sum(sum(1 for j in i if j == 'X') for i in grid)}")


def visit(grid, r, c):
    m, n = len(grid), len(grid[0])
    directions = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))
    visited = set()
    for dr, dc in directions:
        if r not in range(m) or c not in range(n):
            break
        while True:
            r += dr
            c += dc
            if r in range(m) and c in range(n):
                if grid[r][c] == "#":
                    if (r, c, (dr, dc)) in visited:
                        return True
                    visited.add((r, c, (dr, dc)))
                    r -= dr
                    c -= dc
                    break
            else:
                break
    return False


def part2():
    with open("d6.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    m, n = len(grid), len(grid[0])
    r, c = None, None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "^":
                r, c = i, j
                break
    out = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] not in ("^", "#"):
                grid[i][j] = "#"
                has_cycle = visit(grid, r, c)
                out += has_cycle
                grid[i][j] = "."

    print(f"Part2: {out}")


if __name__ == "__main__":
    part1()  # 5086
    part2()  # 1770
