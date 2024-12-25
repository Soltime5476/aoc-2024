from collections import defaultdict


def part1():
    with open("d5.txt") as f:
        g = defaultdict(list)
        s = 0
        while True:
            line = f.readline().strip()
            if line == "":
                break
            u, v = line.split("|")
            g[u].append(v)

        while True:
            line = f.readline().strip()
            if line == "":
                break
            updates = line.split(",")
            prev = []
            proper = True
            for node in updates:
                for prev_nodes in prev:
                    if prev_nodes in g[node]:
                        proper = False
                        break
                prev.append(node)
            if proper:
                s += int(updates[len(updates) // 2])

        print(f"Part1: {s}")


def part2():
    with open("d5.txt") as f:
        g = defaultdict(list)
        s = 0
        while True:
            line = f.readline().strip()
            if line == "":
                break
            u, v = line.split("|")
            g[u].append(v)

        while True:
            line = f.readline().strip()
            if line == "":
                break
            updates = line.split(",")
            prev = []
            proper = True
            for node in updates:
                violated = False
                for i, prev_nodes in enumerate(prev):
                    if prev_nodes in g[node]:
                        proper = False
                        violated = True
                        prev.insert(i, node)
                        break
                if not violated:
                    prev.append(node)

            if not proper:
                s += int(prev[len(prev) // 2])

        print(f"Part2: {s}")


if __name__ == "__main__":
    part1()  # 4872
    part2()  # 5564
