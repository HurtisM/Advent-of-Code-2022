# I was lazy to parse part of input which defined initial stacks, so i just hardcoded it
# and delete this part from input.txt ;-D
#
#Tjhis is how it looks in original input file:
#         [C] [B] [H]
# [W]     [D] [J] [Q] [B]
# [P] [F] [Z] [F] [B] [L]
# [G] [Z] [N] [P] [J] [S] [V]
# [Z] [C] [H] [Z] [G] [T] [Z]     [C]
# [V] [B] [M] [M] [C] [Q] [C] [G] [H]
# [S] [V] [L] [D] [F] [F] [G] [L] [F]
# [B] [J] [V] [L] [V] [G] [L] [N] [J]
#  1   2   3   4   5   6   7   8   9

from copy import deepcopy
FILE_NAME = "input.txt"


def read_file(file_name):
    with open(file_name, "r") as f:
        return [line.strip() for line in f]


def process_lines(lines, crane_fn, stacks):
    for line in lines:
        kolko, odkial, kam = map(int, line.split()[1:6:2])
        crane_fn(kolko, odkial, kam, stacks)


initial_stacks = {
    1: ["B", "S", "V", "Z", "G", "P", "W"],
    2: ["J", "V", "B", "C", "Z", "F"],
    3: ["V", "L", "M", "H", "N", "Z", "D", "C"],
    4: ["L", "D", "M", "Z", "P", "F", "J", "B"],
    5: ["V", "F", "C", "G", "J", "B", "Q", "H"],
    6: ["G", "F", "Q", "T", "S", "L", "B"],
    7: ["L", "G", "C", "Z", "V"],
    8: ["N", "L", "G"],
    9: ["J", "F", "H", "C"],
}


def crane1(kolko, odkial, kam, stacks):
    dest = stacks[kam]
    src = stacks[odkial]
    for _ in range(kolko):
        dest.append(src.pop())


def crane2(kolko, odkial, kam, stacks):
    dest = stacks[kam]
    src = stacks[odkial]
    moved = src[-kolko:]
    del src[-kolko:]
    dest.extend(moved)


if __name__ == "__main__":
    lines = read_file(FILE_NAME)

    stacks1 = deepcopy(initial_stacks)
    process_lines(lines, crane1, stacks1)
    print("Part1:", "".join(stacks1[i][-1] for i in range(1, 10)))

    stacks2 = deepcopy(initial_stacks)
    process_lines(lines, crane2, stacks2)
    print("Part1:", "".join(stacks2[i][-1] for i in range(1, 10)))