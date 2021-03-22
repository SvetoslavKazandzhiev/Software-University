matrix = [list(input().replace(' ', '')) for _ in range(8)]


def find_k():
    row_index = 0
    for row in matrix:
        col_index = 0
        for col in row:
            if col == 'K':
                return row_index, col_index
            col_index += 1
        row_index += 1


def show_matrix(matrix):
    for row in matrix:
        for field in row:
            print(field, end='')
        print()


def move(king_coords):
    output = []
    row = king_coords[0]
    col = king_coords[1]
    while row >= 0:
        if matrix[row][king_coords[1]] == 'Q':
            output.append([row, col])
            break
        row -= 1
    row = king_coords[0]
    col = king_coords[1]
    while row >= 0 and col <= 7:
        if matrix[row][col] == 'Q':
            output.append([row, col])
            break
        row -= 1
        col += 1
    row = king_coords[0]
    col = king_coords[1]
    while row <= 7:
        if matrix[row][col] == 'Q':
            output.append([row, col])
            break
        row += 1
    return output
king_coords = find_k()

print(move(king_coords))