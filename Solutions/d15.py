def move(grid, i, j, di, dj):
    if grid[i][j] == "#":
        return i, j
    elif grid[i][j] == ".":
        return i + di, j + dj

    i1, j1 = move(grid, i + di, j + dj, di, dj)
    if (i1, j1) != (i + di, j + dj):
        grid[i + di][j + dj] = grid[i][j]
        grid[i][j] = "."
        return i + di, j + dj

    return i, j


def move_p2(grid, i, j, di, dj):
    if grid[i][j] == "#":
        return i, j, False
    elif grid[i][j] == ".":
        return i, j, True

    success = False
    b = grid[i + di][j + dj]
    if di == 0 or b not in "[]":
        success = move_p2(grid, i + di, j + dj, di, dj)[-1]
    else:
        success = push_boxes_vertical(grid, i + di, j + dj, di, dj)

    if success:
        grid[i + di][j + dj], grid[i][j] = grid[i][j], grid[i + di][j + dj]
        i += di
        j += dj

    return i, j, success


def push_boxes_vertical(grid, i, j, di, dj):
    boxes = []
    r = set()
    r.add((i, j))
    if grid[i][j] == "[":
        r.add((i, j + 1))
    else:
        r.add((i, j - 1))

    while r:
        next_r = set()
        boxes.append(r)

        for i, j in r:
            b = grid[i + di][j + dj]
            if b == "#":
                return False
            elif b == "[":
                next_r.add((i + di, j + dj))
                next_r.add((i + di, j + dj + 1))
            elif b == "]":
                next_r.add((i + di, j + dj))
                next_r.add((i + di, j + dj - 1))

        r = next_r

    for b in reversed(boxes):
        for x, y in b:
            grid[x + di][y + dj], grid[x][y] = grid[x][y], grid[x + di][y + dj]

    return True


def part1():
    with open("d15.txt") as f:
        grid = []
        while True:
            line = f.readline().strip()
            if line != "":
                grid.append(list(line))
            else:
                moves = "".join(line.strip() for line in f.readlines())
                break

    m = len(grid)
    n = len(grid[0])
    r, c = None, None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                r, c = i, j
                break
        if r is not None:
            break

    adj = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}
    for mv in moves:
        dr, dc = adj[mv]
        r, c = move(grid, r, c, dr, dc)

    s = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "O":
                s += i * 100 + j
    print(f"Part1: {s}")


def part2():
    with open("d15.txt") as f:
        grid = []
        new = {"#": "##", "O": "[]", ".": "..", "@": "@."}
        while True:
            line = f.readline().strip()
            if line != "":
                grid.append(list("".join(new[i] for i in line)))
            else:
                moves = "".join(line.strip() for line in f.readlines())
                break

    m = len(grid)
    n = len(grid[0])
    r, c = None, None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                r, c = i, j
                break
        if r is not None:
            break

    adj = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}
    for mv in moves:
        dr, dc = adj[mv]
        r, c, _ = move_p2(grid, r, c, dr, dc)

    s = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "[":
                s += 100 * i + j

    print(f"Part2 {s}")


if __name__ == "__main__":
    part1()  # 1349898
    part2()  # 1376686
