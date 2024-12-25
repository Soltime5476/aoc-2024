def part1():
    with open("d17.txt") as f:
        A = int(f.readline().split(": ")[1])
        B = int(f.readline().split(": ")[1])
        C = int(f.readline().split(": ")[1])
        f.readline()
        program = [int(i) for i in f.readline().split(": ")[1].split(",")]

    out = []
    ptr = 0
    while ptr < len(program):
        opcode, operand = program[ptr], program[ptr + 1]

        if operand in (4, 5, 6):
            combo_operand = (A, B, C)[operand - 4]
        else:
            combo_operand = operand

        jmp = False
        if opcode == 0:
            A >>= combo_operand
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = combo_operand & 7
        elif opcode == 3 and A:
            ptr = operand
            jmp = True
        elif opcode == 4:
            B ^= C
        elif opcode == 5:
            out.append(str(combo_operand & 7))
        elif opcode == 6:
            B = A >> combo_operand
        elif opcode == 7:
            C = A >> combo_operand

        if not jmp:
            ptr += 2

    print(f"Part1: {','.join(out)}")


def three_bits(n):
    return bin(n)[2:].zfill(3)


def brute_p2(program, i, bits):
    if i == len(program):
        b = "".join(i for i in bits if i is not None)
        return int(b, base=2)

    target = program[i]
    start = 128 - 3 * (i + 1)
    ret = float("inf")

    # try every A % 8
    for j in range(8):
        to_undo = []
        failed = False
        b = three_bits(j)
        for k in range(3):
            if bits[start + k] is None:
                to_undo.append(start + k)
                bits[start + k] = b[k]
            elif bits[start + k] != b[k]:
                failed = True
                break

        if not failed:
            offset = j ^ 3
            offset_start = start - offset
            b = three_bits(target ^ j ^ 7)
            for k in range(3):
                if bits[offset_start + k] is None:
                    to_undo.append(offset_start + k)
                    bits[offset_start + k] = b[k]
                elif bits[offset_start + k] != b[k]:
                    failed = True
                    break

        if not failed:
            ret = min(ret, brute_p2(program, i + 1, bits))
        for p in to_undo:
            bits[p] = None

    return ret


def part2():
    # solution specific to my input only!
    with open("d17.txt") as f:
        A = int(f.readline().split(": ")[1])
        B = int(f.readline().split(": ")[1])
        C = int(f.readline().split(": ")[1])
        f.readline()
        program = [int(i) for i in f.readline().split(": ")[1].split(",")]

    initial_A = brute_p2(program, 0, [None] * 128)
    print(f"Part2: {initial_A}")


if __name__ == "__main__":
    part1()  # 2,1,4,7,6,0,3,1,4
    part2()  # 266932601404433
