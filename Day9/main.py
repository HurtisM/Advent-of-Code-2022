FILE_NAME = "input.txt"


def read_file(file_name):
    with open(file_name) as f:
        return [(d, int(n)) for d, n in (line.split() for line in f)]


def adjust(H, T):
    dr = (H[0] - T[0])
    dc = (H[1] - T[1])

    if abs(dr) <= 1 and abs(dc) <= 1:
        pass
    elif abs(dr) >= 2 and abs(dc) >= 2:
        T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1] - 1 if T[1] < H[1] else H[1] + 1)
    elif abs(dr) >= 2:
        T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1])
    elif abs(dc) >= 2:
        T = (H[0], H[1] - 1 if T[1] < H[1] else H[1] + 1)
    return T


if __name__ == "__main__":
    coordinates = read_file(FILE_NAME)
   
    H = (0, 0)
    T = [(0, 0) for _ in range(9)]

    DR = {
        'L': 0,
        'U': -1,
        'R': 0,
        'D': 1
    }
    DC = {
        'L': -1,
        'U': 0,
        'R': 1,
        'D': 0
    }

    TPOS1 = set()
    TPOS2 = set()

    for coordinate in coordinates:
        for _ in range(coordinate[1]):
            TPOS1.add(T[0])
            TPOS2.add(T[8])
            H = (H[0] + DR[coordinate[0]], H[1] + DC[coordinate[0]])
            T[0] = adjust(H, T[0])
            for i in range(1, 9):
                T[i] = adjust(T[i - 1], T[i])
            TPOS1.add(T[0])
            TPOS2.add(T[8])

    print(len(TPOS1))
    print(len(TPOS2))
