def part1():
    instructions = []
    wires = {}
    with open("d24.txt") as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            w, n = line.strip().split(": ")
            wires[w] = int(n)
        for line in f:
            op, dest = line.strip().split(" -> ")
            a, b, c = op.split(" ")
            instructions.append(((a, b, c), dest))

    while True:
        done = True
        for (a, b, c), dest in instructions:
            if a not in wires or c not in wires:
                done = False
                continue
            elif b == "AND":
                wires[dest] = wires[a] & wires[c]
            elif b == "OR":
                wires[dest] = wires[a] | wires[c]
            else:
                wires[dest] = wires[a] ^ wires[c]
        if done:
            break

    vals = sorted(((i, j) for i, j in wires.items() if i[0] == "z"), reverse=True)
    bits = "".join(str(bit) for _, bit in vals)
    print(f"Part1: {int(bits, base=2)}")


def find_dest(instructions, a, b, op):
    for (i, j, k), dest in instructions:
        if (a, op, b) in ((i, j, k), (k, j, i)):
            return dest
    return None


def part2():
    instructions = []
    wires = {}

    with open("d24.txt") as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            w, n = line.strip().split(": ")
            wires[w] = int(n)
        for line in f:
            op, dest = line.strip().split(" -> ")
            a, b, c = op.split(" ")
            instructions.append(((a, b, c), dest))

    bits = sum(1 for i in wires if i[0] == "x")
    swaps = set()
    cin = None
    for b in range(bits):
        """Full Adder Operations
        let xi, yi be input bits, cin be carry bits, zi be output bit
        first half adder:
        M = xi ^ yi, N = xi & yi
        second half adder:
        zi = M ^ cin, R = M & cin
        or gate for next carry bit:
        cout = R | N
        carry cout as cin for adding the next bit
        """
        xi = "x" + str(b).zfill(2)
        yi = "y" + str(b).zfill(2)
        zi = "z" + str(b).zfill(2)
        M = find_dest(instructions, xi, yi, "XOR")
        N = find_dest(instructions, xi, yi, "AND")
        if cin is None:
            # first bit is only a half adder with Z = xi ^ yi and cout = xi & yi
            Z = find_dest(instructions, xi, yi, "XOR")
            cout = N
        else:
            R = find_dest(instructions, M, cin, "AND")
            if R is None:
                # output of M and N are swapped
                R = find_dest(instructions, N, cin, "AND")
                M, N = N, M
                swaps.update((M, N))

            Z = find_dest(instructions, M, cin, "XOR")
            if Z != zi:
                if M == zi:
                    Z, M = M, Z
                    swaps.update((Z, M))
                elif N == zi:
                    Z, N = N, Z
                    swaps.update((Z, N))
                elif R == zi:
                    Z, R = R, Z
                    swaps.update((Z, R))

            cout = find_dest(instructions, R, N, "OR")

        if cout == zi:
            cout, Z = Z, cout
            swaps.update((Z, cout))
        cin = cout

    print(f"Part2: {','.join(sorted(swaps))}")


if __name__ == "__main__":
    part1()  # 65635066541798
    part2()  # dgr,dtv,fgc,mtj,vvm,z12,z29,z37
