import sys
from collections import deque

# --- Read input ---
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(infile).read().strip()
lines = data.split("\n")

rows = len(lines)
cols = len(lines[0])

# Convert grid to elevation map
grid = [list(line) for line in lines]
elevations = [[0 for _ in range(cols)] for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        ch = grid[r][c]
        if ch == "S":
            elevations[r][c] = 1
        elif ch == "E":
            elevations[r][c] = 26
        else:
            elevations[r][c] = ord(ch) - ord("a") + 1


def bfs(part: int) -> int:

    queue = deque()

    # find start positions
    for r in range(rows):
        for c in range(cols):
            if (part == 1 and grid[r][c] == "S") or (part == 2 and elevations[r][c] == 1):
                queue.append(((r, c), 0))  # ((row, col), distance)

    visited = set()

    while queue:
        (r, c), dist = queue.popleft()

        if (r, c) in visited:
            continue
        visited.add((r, c))

        # goal check
        if grid[r][c] == "E":
            return dist

        # explore neighbors
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr, cc = r + dr, c + dc
            if (
                0 <= rr < rows
                and 0 <= cc < cols
                and elevations[rr][cc] <= elevations[r][c] + 1
            ):
                queue.append(((rr, cc), dist + 1))


print("Part 1:", bfs(1))
print("Part 2:", bfs(2))
