from functools import cache


@cache
def cal_stones(n, rep):
    if rep == 0:
        return 1
    s = str(n)
    rep -= 1
    if n == 0:
        return cal_stones(1, rep)
    elif len(s) % 2:
        return cal_stones(n * 2024, rep)
    else:
        return cal_stones(int(s[: len(s) // 2]), rep) + cal_stones(int(s[len(s) // 2 :]), rep)


def part1():
    with open("d11.txt") as f:
        stones = [int(i) for i in f.read().split()]

    for _ in range(25):
        new_stones = []
        for j in stones:
            s = str(j)
            if j == 0:
                new_stones.append(1)
            elif len(s) % 2 == 0:
                new_stones.append(int(s[: len(s) // 2]))
                new_stones.append(int(s[len(s) // 2 :]))
            else:
                new_stones.append(j * 2024)

        stones = new_stones
    print(f"Part1: {len(new_stones)}")


def part2():
    with open("d11.txt") as f:
        stones = [int(i) for i in f.read().split()]
    print(f"Part2: {sum(cal_stones(i, 75) for i in stones)}")


if __name__ == "__main__":
    part1()  # 199982
    part2()  # 237149922829154
