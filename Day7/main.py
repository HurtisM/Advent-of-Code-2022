FILE_NAME = "input.txt"
from collections import defaultdict


def read_file(file_name):
    with open(file_name, "r") as f:
        return [line.strip() for line in f]


def process_commands(commands):
    SZ = defaultdict(int)
    cesta = []
    for command in commands:
        slovo = command.strip().split()
        if slovo[1] == 'cd':
            if slovo[2] == '..':
                cesta.pop()
            else:
                cesta.append(slovo[2])
        elif slovo[1] == 'ls':
            continue
        else:
            try:
                sz = int(slovo[0])
                for i in range(len(cesta) + 1):
                    SZ['/'.join(cesta[:i])] += sz
            except:
                pass

    max_used = 70000000 - 30000000
    total_used = SZ['/']
    need_to_free = total_used - max_used

    best = 1e9

    ans = 0
    for k, v in SZ.items():
        if v >= need_to_free:
            best = min(best, v)
        if v <= 100000:
            ans += v
    return ans, best


if __name__ == "__main__":
    data = (read_file(FILE_NAME))
    print(process_commands(data))
