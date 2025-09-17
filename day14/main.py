FILE_NAME = "input.txt"


def read_file(file_name):
    with open(file_name, "r") as f:
        x = []
        for line in f:
            x.append([list(map(int, p.split(","))) for p in line.strip().split(" -> ")])
        return x


def process_pairs(pairs):
    blocks = set()
    abyss = 0
    for pair in pairs:
        for (x1, y1), (x2, y2) in zip(pair, pair[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    blocks.add(x + y * 1j)
                    abyss = max(abyss, y + 1)
    return blocks, abyss


def calculate_sand_units(blocks, abyss):
    units = 0
    while 500 not in blocks:
        sand = 500
        while True:
            if sand.imag >= abyss:
                return units

            if sand + 1j not in blocks:
                sand += 1j
                continue
            if sand + 1j - 1 not in blocks:
                sand += 1j - 1
                continue
            if sand + 1j + 1 not in blocks:
                sand += 1j + 1
                continue
            break
        blocks.add(sand)
        units += 1
    return units


def calculate_sand_units2(blocks, abyss):
    units = 0
    while 500 not in blocks:
        sand = 500
        while True:
            if sand.imag >= abyss:
                break
            if sand + 1j not in blocks:
                sand += 1j
                continue
            if sand + 1j - 1 not in blocks:
                sand += 1j - 1
                continue
            if sand + 1j + 1 not in blocks:
                sand += 1j + 1
                continue
            break
        blocks.add(sand)
        units += 1
    return units


if __name__ == "__main__":
    pairs = read_file(FILE_NAME)
    blocks, abyss = process_pairs(pairs)
    print(calculate_sand_units(blocks, abyss))
    print(calculate_sand_units2(blocks, abyss))



