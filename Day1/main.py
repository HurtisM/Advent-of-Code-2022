FILE_NAME = "input.txt"


def load_data(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    return lines


def process_elfs(lines):
    elves = []
    elf = []

    for line in lines:
        if line == '\n':
            elves += [sum(elf)]
            elf = []
            continue
        elf += [int(line)]
    elves += [sum(elf)]
    return elves


if __name__ == "__main__":
    data = load_data(FILE_NAME)
    elfs = process_elfs(data)
    elfs = sorted(elfs, reverse=True)
    print(elfs)
    print(f"Part1: {elfs[0]}")
    print(f"Part2: {sum(elfs[:3])}")
