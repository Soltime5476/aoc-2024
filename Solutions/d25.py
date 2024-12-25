def part1():
    keys = []
    locks = []
    with open("d25.txt") as f:
        while True:
            heights = [0, 0, 0, 0, 0]
            fig = [list(f.readline().strip()) for _ in range(7)]
            if not fig[0]:
                break

            for j in range(5):
                for i in range(1, 6):
                    if fig[i][j] == "#":
                        heights[j] += 1

            if fig[0][0] == ".":
                keys.append(heights)
            else:
                locks.append(heights)
            f.readline()

        total = 0
        for k in keys:
            for l in locks:
                if all(i + j <= 5 for i, j in zip(l, k)):
                    total += 1

        print(f"Part1: {total}")


if __name__ == "__main__":
    part1()  # 3223
