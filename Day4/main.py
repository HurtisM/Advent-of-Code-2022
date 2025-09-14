FILE_NAME = "input.txt"


def read_file(file_name):
    sections =[]
    with open(file_name, "r") as f:
        for line in f:
            sections.append(line.strip())
    return sections


def part1(sections):
    overlapping = 0
    for section in sections:
        first, second = section.split(',')
        f1, f2 = first.split('-')
        s1, s2 = second.split('-')
        f1, f2, s1, s2 = [int(x) for x in [f1, f2, s1, s2]]
        if f1 <= s1 and f2 >= s2 or f1 >= s1 and f2 <= s2:
            overlapping += 1
    return overlapping


def part2(sections):
    overlapping = 0
    for section in sections:
        first, second = section.split(',')
        f1, f2 = first.split('-')
        s1, s2 = second.split('-')
        f1, f2, s1, s2 = [int(x) for x in [f1, f2, s1, s2]]
        if not (f1 > s2 or f2 < s1):
            overlapping += 1
    return overlapping


if __name__ == "__main__":
    data = read_file(FILE_NAME)
    print(part1(data))
    print(part2(data))
