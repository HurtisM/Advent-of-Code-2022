FILE_NAME = "input.txt"


def read_file(file_name):
    with open(file_name) as f:
        pairs = []
        for line in f:
            path = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
            pairs.append(path)
        return pairs


def process_pairs(pairs):
    """Return set of blocked positions and max y (abyss)"""
    blocks = set()
    max_y = 0
    for path in pairs:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    blocks.add(x + y * 1j)
                    max_y = max(max_y, y)
    return blocks, max_y


def simulate_sand(blocks, abyss):
    """Simulate sand falling and return number of units + final grid"""
    units = 0

    # Determine bounds for the grid
    min_x = int(min(b.real for b in blocks)) - 1
    max_x = int(max(b.real for b in blocks)) + 1
    max_y_grid = abyss + 1

    width = max_x - min_x + 1
    height = max_y_grid + 1

    # Create grid filled with "."
    grid = [["." for _ in range(width)] for _ in range(height)]

    # Draw walls
    for block in blocks:
        x, y = int(block.real) - min_x, int(block.imag)
        grid[y][x] = "#"

    # Simulate sand
    while 500 not in blocks:
        sand = 500 + 0j
        while True:
            if sand.imag >= abyss:
                # Sand falls into the abyss
                return units, grid

            # Try moving down
            if sand + 1j not in blocks:
                sand += 1j
                continue
            # Try down-left
            if sand + 1j - 1 not in blocks:
                sand += 1j - 1
                continue
            # Try down-right
            if sand + 1j + 1 not in blocks:
                sand += 1j + 1
                continue
            break

        blocks.add(sand)
        x, y = int(sand.real) - min_x, int(sand.imag)
        grid[y][x] = "o"
        units += 1

    return units, grid

def simulate_sand_part2(blocks, abyss):
    """Simulate sand falling with infinite floor (Part 2)"""
    units = 0
    floor_y = abyss + 2  # infinite floor

    # Determine bounds for the grid (make it wider to fit sand spreading)
    min_x = int(min(b.real for b in blocks)) - floor_y - 1
    max_x = int(max(b.real for b in blocks)) + floor_y + 1
    max_y_grid = floor_y

    width = max_x - min_x + 1
    height = max_y_grid + 1

    # Create grid
    grid = [["." for _ in range(width)] for _ in range(height)]

    # Draw walls
    for block in blocks:
        x, y = int(block.real) - min_x, int(block.imag)
        grid[y][x] = "#"

    # Draw floor
    for x in range(width):
        grid[floor_y][x] = "#"

    # Simulate sand
    while 500 + 0j not in blocks:
        sand = 500 + 0j
        while True:
            if sand + 1j not in blocks and sand.imag + 1 < floor_y:
                sand += 1j
                continue
            if sand + 1j - 1 not in blocks and sand.imag + 1 < floor_y:
                sand += 1j - 1
                continue
            if sand + 1j + 1 not in blocks and sand.imag + 1 < floor_y:
                sand += 1j + 1
                continue
            break

        blocks.add(sand)
        x, y = int(sand.real) - min_x, int(sand.imag)
        grid[y][x] = "o"
        units += 1

    return units, grid



if __name__ == "__main__":
    pairs = read_file(FILE_NAME)
    blocks, abyss = process_pairs(pairs)

    part1_units, part1_grid = simulate_sand(blocks.copy(), abyss)
    print("Part 1 units:", part1_units)

    # Print grid
    for row in part1_grid:
        print("".join(row))

    part2_units, part2_grid = simulate_sand_part2(blocks.copy(), abyss)
    print("Part 2 units:", part2_units)

    for row in part2_grid:
        print("".join(row))