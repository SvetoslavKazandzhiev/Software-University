def read_matrix():
    size = int(input())
    matrix = []
    for row in range(size):
        matrix.append([0] * size)
    return matrix


def show_matrix(matrix):
    for row in matrix:
        idx = 0
        for field in row:
            if idx == len(matrix) - 1:
                print(field, end='')
                continue
            print(field, end=' ')
            idx += 1
        print()

matrix = read_matrix()


def get_bombs():
    bomb_num = int(input())
    bombs = []
    for i in range(bomb_num):
        bomb_str = input()

        bombs.append((int(bomb_str[1]), int(bomb_str[4])))

    return bombs


def place_bombs(matrix):
    for bomb in bombs:
        matrix[bomb[0]][bomb[1]] = '*'


def numbers(field_coords):
    row = field_coords[0]
    col = field_coords[1]
    count = 0
    if row -1 >= 0:
        if matrix[row - 1][col] == '*':
            count += 1
    if row -1 >= 0 and col + 1 < len(matrix):
        if matrix[row - 1][col+1] == '*':
            count += 1
    if col + 1 < len(matrix):
        if matrix[row][col+1] == '*':
            count += 1
    if row +1 < len(matrix) and col + 1 < len(matrix):
        if matrix[row + 1][col+1] == '*':
            count += 1
    if row +1 < len(matrix):
        if matrix[row + 1][col] == '*':
            count += 1
    if row +1 < len(matrix) and col - 1 >= 0:
        if matrix[row + 1][col-1] == '*':
            count += 1
    if col - 1 >= 0:
        if matrix[row][col-1] == '*':
            count += 1
    if row - 1 >= 0 and col - 1 >= 0:
        if matrix[row - 1][col-1] == '*':
            count += 1
    return count


def detects_bombs():
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] != '*':
                matrix[row][col] = numbers((row, col))


bombs = get_bombs()
place_bombs(matrix)
detects_bombs()
show_matrix(matrix)