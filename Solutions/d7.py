def brutep1(target, s, nums, i):
    if i == len(nums) - 1:
        return target == s
    return brutep1(target, s + nums[i + 1], nums, i + 1) or brutep1(
        target, s * nums[i + 1], nums, i + 1
    )


def brutep2(target, s, nums, i):
    if i == len(nums) - 1:
        return target == s
    return (
        brutep2(target, s + nums[i + 1], nums, i + 1)
        or brutep2(target, s * nums[i + 1], nums, i + 1)
        or brutep2(target, int(str(s) + str(nums[i + 1])), nums, i + 1)
    )


def part1():
    s = 0
    with open("d7.txt") as f:
        for line in f:
            target, nums = line.split(": ")
            target = int(target)
            nums = [int(i) for i in nums.split()]
            if brutep1(target, nums[0], nums, 0):
                s += target
    print(f"Part1: {s}")


def part2():
    s = 0
    with open("d7.txt") as f:
        for line in f:
            target, nums = line.split(": ")
            target = int(target)
            nums = [int(i) for i in nums.split()]
            if brutep2(target, nums[0], nums, 0):
                s += target
    print(f"Part2: {s}")


if __name__ == "__main__":
    part1()  # 5030892084481
    part2()  # 91377448644679
