def part1():
    with open("d9.txt") as f:
        disk = f.read().strip()
    blocks = [int(i) for i in disk[::2]]
    spaces = [int(i) for i in disk[1::2]]
    compact = []
    left = 0
    right = len(blocks) - 1
    while left < right:
        compact += [left] * blocks[left]
        while spaces[left] >= blocks[right]:
            compact += [right] * blocks[right]
            spaces[left] -= blocks[right]
            right -= 1

        compact += [right] * spaces[left]
        blocks[right] -= spaces[left]
        left += 1

    compact += [left] * blocks[left]
    print(f"Part1: {sum(i * j for i, j in enumerate(compact))}")


def part2():
    with open("d9.txt") as f:
        disk = f.read().strip()

    blocks = [int(i) for i in disk[::2]]
    spaces = [int(i) for i in disk[1::2]] + [0]
    buffer = [[] for _ in range(len(blocks))]
    for right in range(len(blocks) - 1, -1, -1):
        for left in range(right):
            if spaces[left] >= blocks[right]:
                spaces[left] -= blocks[right]
                spaces[right - 1] += blocks[right]
                buffer[left] += [right] * blocks[right]
                blocks[right] = 0
                break

    compact = []
    for i in range(len(blocks)):
        compact += [i] * blocks[i]
        compact += buffer[i] + [0] * (spaces[i])
    print(f"Part2: {sum(i * j for i, j in enumerate(compact))}")


if __name__ == "__main__":
    part1()  # 6395800119709
    part2()  # 6418529470362
