import re


def part1():
    with open("d3.txt") as f:
        mem = f.read()
    instructions = re.findall(r"mul\([0-9]+,[0-9]+\)", mem)
    s = 0
    for i in instructions:
        a, b = map(int, i[4:-1].split(","))
        s += a * b

    print(f"Part1: {s}")


def part2():
    with open("d3.txt") as f:
        mem = f.read()
    instructions = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", mem)
    do = True
    s = 0
    for i in instructions:
        if i == "don't()":
            do = False
        elif i == "do()":
            do = True
        elif do:
            a, b = map(int, i[4:-1].split(","))
            s += a * b

    print(f"Part2: {s}")


if __name__ == "__main__":
    part1()  # 187194524
    part2()  # 127092535
