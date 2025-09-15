FILE_NAME = "input.txt"


def read_file(file_name):
    result = []
    with open(file_name) as f:
        for line in f:
            parts = line.split()
            if len(parts) == 1:  # "noop"
                result.append((parts[0], None))
            else:  # "addx n"
                result.append((parts[0], int(parts[1])))
    return result


def proces_signal(signal):
    X = 1
    cycle = 0
    output = []
    output.append([cycle, X])
    for instruction in signal:
        if instruction[0] == 'noop':
            cycle += 1
            output.append([cycle, X])
        elif instruction[0] == 'addx':
            cycle += 1
            output.append([cycle, X])
            cycle += 1
            output.append([cycle, X])
            X = X + int(instruction[1])

    sum = 0
    for n in (20, 60, 100, 140, 180, 220):
        sum += (output[n][0] * output[n][1])
    return sum


def crt_drawing(signal):
    CRT = list(240*" ")
    cycle = 0
    sprite_pos = 1
    for instruction in signal:
        if instruction[0] == 'noop':
            crt_pos = cycle % 40
            if sprite_pos - 1 <= crt_pos <= sprite_pos + 1:
                CRT[cycle] = '#'
            cycle += 1

        elif instruction[0] == 'addx':
            crt_pos = cycle % 40
            if sprite_pos - 1 <= crt_pos <= sprite_pos + 1:
                CRT[cycle] = '#'
            cycle += 1
            crt_pos = cycle % 40
            if sprite_pos - 1 <= crt_pos <= sprite_pos + 1:
                CRT[cycle] = '#'
            cycle += 1
            sprite_pos += int(instruction[1])
    return CRT


if __name__ == "__main__":
    signal = read_file(FILE_NAME)
    print(proces_signal(signal))

    s = crt_drawing(signal)
    for i in range(0, len(s), 40):
        print("".join(s[i:i + 40]))




