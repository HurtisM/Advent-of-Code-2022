FILE_NAME = "input.txt"

matrix_case1 = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]
matrix_case2 = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]

coordinates = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2
}


def calculate_score(file_name, matrix):
    score = 0
    with open(file_name) as f:
        for line in f:
            xcor, ycor = line.split()
            score += (matrix[coordinates[xcor]][coordinates[ycor]])
        return score


if __name__ == "__main__":
    print(calculate_score(FILE_NAME, matrix_case1))
    print(calculate_score(FILE_NAME, matrix_case2))
