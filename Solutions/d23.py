from collections import defaultdict
from itertools import combinations


def find_cliques(R, P, X, G):
    # https://en.wikipedia.org/wiki/Bron–Kerbosch_algorithm
    cliques = []

    def helper(R, P, X):
        if not P and not X:
            cliques.append(R)
            return
        pivot = max(P | X, key=lambda u: len(G[u]))
        for v in P - G[pivot]:
            helper(R | set([v]), P & G[v], X & G[v])
            P.remove(v)
            X.add(v)

    helper(R, P, X)
    return cliques


def part1():
    g = defaultdict(set)
    with open("d23.txt") as f:
        for line in f:
            u, v = line.strip().split("-")
            g[u].add(v)
            g[v].add(u)

    total = 0
    for a, b, c in combinations(g, r=3):
        if "t" not in (a[0], b[0], c[0]):
            continue
        elif b in g[a] and c in g[b] and a in g[c]:
            total += 1

    print(f"Part1: {total}")


def part2():
    g = defaultdict(set)
    degrees = defaultdict(int)
    with open("d23.txt") as f:
        for line in f:
            u, v = line.strip().split("-")
            g[u].add(v)
            g[v].add(u)
            degrees[u] += 1
            degrees[v] += 1

    R = set()
    P = set(g)
    X = set()
    maximal_cliques = find_cliques(R, P, X, g)
    largest_clique = max(maximal_cliques, key=len)
    print(f"Part2: {','.join(sorted(largest_clique))}")


if __name__ == "__main__":
    part1()  # 1467
    part2()  # di,gs,jw,kz,md,nc,qp,rp,sa,ss,uk,xk,yn
