from functools import cache


def wordBreak(s: str, wordDict: tuple[str]) -> int:
    @cache
    def helper(s: str):
        if not s:
            return 1
        out = 0
        for i in wordDict:
            m = len(i)
            if s.startswith(i):
                out += helper(s[m:])
        return out

    return helper(s)


def part1():
    with open("d19.txt") as f:
        wordDict = tuple(f.readline().strip().split(", "))
        f.readline()
        s = 0
        for line in f:
            if wordBreak(line.strip(), wordDict):
                s += 1
        print(f"Part1: {s}")


def part2():
    with open("d19.txt") as f:
        wordDict = tuple(f.readline().strip().split(", "))
        f.readline()
        s = 0
        for line in f:
            s += wordBreak(line.strip(), wordDict)
    print(f"Part2: {s}")


if __name__ == "__main__":
    part1()  # 308
    part2()  # 662726441391898
