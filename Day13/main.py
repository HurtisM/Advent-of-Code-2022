import ast
from functools import cmp_to_key

FILE_NAME = "input.txt"


def read_file(file_name):
    with open(file_name) as f:
        return [line.strip() for line in f]


def compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        return -1 if p1 < p2 else (1 if p1 > p2 else 0)

    if isinstance(p1, list) and isinstance(p2, list):
        for a, b in zip(p1, p2):
            res = compare(a, b)
            if res != 0:
                return res
        return -1 if len(p1) < len(p2) else (1 if len(p1) > len(p2) else 0)

    if isinstance(p1, int):
        return compare([p1], p2)
    return compare(p1, [p2])


def part1(lines):
    part1_sum = 0
    pair_index = 1  # 1-based index

    for i in range(0, len(lines), 3):  # each block has 2 lines + blank
        left = ast.literal_eval(lines[i])
        right = ast.literal_eval(lines[i + 1])
        if compare(left, right) == -1:
            part1_sum += pair_index
        pair_index += 1
    return part1_sum


def part2(lines):
    packets = []

    for line in lines:
        if line:
            packets.append(ast.literal_eval(line))

    # Add divider packets
    div1 = [[2]]
    div2 = [[6]]
    packets.extend([div1, div2])

    # Sort with custom comparator
    packets.sort(key=cmp_to_key(compare))

    # Find positions (1-based)
    pos1 = packets.index(div1) + 1
    pos2 = packets.index(div2) + 1

    return pos1 * pos2


if __name__ == "__main__":
    data = read_file(FILE_NAME)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
