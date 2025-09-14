FILE_NAME = "input.txt"


def evaluate_items(file_name):
    ans = 0
    with open(file_name) as f:
        for line in f:
            x = line.strip()
            y = x[:len(x)//2]
            z = x[len(x)//2:]
            for char in y:
                if char in z:
                    if 'a' <= char <= 'z':
                        ans += ord(char)-ord('a')+1
                    else:
                        ans += ord(char)-ord('A')+27
                    break
    return ans


def evaluate_badges(file_name):
    ans = 0
    row = [line for line in open(file_name)]
    number_of_lines = len(row)
    i = 0
    while i < number_of_lines:
        for char in row[i]:
            if char in row[i+1] and char in row[i+2]:
                if 'a' <= char <= 'z':
                    ans += ord(char)-ord('a')+1
                else:
                    ans += ord(char)-ord('A')+27
                break
        i += 3
    return ans


if __name__ == "__main__":
    print(evaluate_items(FILE_NAME))
    print(evaluate_badges(FILE_NAME))