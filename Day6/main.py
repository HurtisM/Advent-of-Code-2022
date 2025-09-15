FILE_NAME = "input.txt"


def read_file(file_name):
    with open(file_name) as f:
        return f.readline().strip()


def find_marker(data, num_of_char):
    for i in range(len(data)):
        if i - num_of_char - 1 >= 0 and len(set([data[i - j] for j in range(num_of_char)])) == num_of_char:
            print(i + 1)
            break


if __name__ == "__main__":
    datastream = (read_file(FILE_NAME))

    find_marker(datastream, 4)
    find_marker(datastream, 14)
