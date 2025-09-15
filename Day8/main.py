FILE_NAME = "input.txt"

def read_file(file_name):
    rows = []
    with open(file_name, "r") as f:
        for line in f:
            rows.append([int(x) for x in line.strip()])
    return rows


def part_1(rows):
    tree = 0
    nrows, ncols = len(rows), len(rows[0])
    for r in range(nrows):
        for c in range(ncols):
            k = rows[r][c]

            directions = [
                (rows[r][:c]),  # left
                (rows[r][c + 1:]),  # right
                [rows[x][c] for x in range(r)],  # up
                [rows[x][c] for x in range(r + 1, nrows)]  # down
            ]
            if any(all(val < k for val in d) for d in directions):
                tree += 1
    return tree


def part_2(rows):
    tree = 0
    nrows, ncols = len(rows), len(rows[0])
    for r in range(nrows):
        for c in range(ncols):
            k = rows[r][c]
            left = viewing_distance(reversed(rows[r][:c]), k)
            right = viewing_distance(rows[r][c + 1:], k)
            up = viewing_distance(reversed([rows[x][c] for x in range(r)]), k)
            down = viewing_distance([rows[x][c] for x in range(r + 1, nrows)], k)
            if (left * right * up * down) > tree:
                tree = left * right * up * down
    return tree


def viewing_distance(line, height):
    count = 0
    for h in line:
        count += 1
        if h >= height:
            break
    return count


if __name__ == "__main__":
    data = (read_file(FILE_NAME))
    print(part_1(data))
    print(part_2(data))
