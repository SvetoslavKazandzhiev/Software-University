def read_matrix():
    rows_count = int(input())
    matrix = []
    for row_index in range(rows_count):
        row = input().replace('\n', '')
        new_row = []
        elements = ''
        for ch in row:

            if ch == ' ':
                if elements.isnumeric():
                    elements = int(elements)
                new_row.append(elements)
                elements = ''
            else:
                elements += ch
        if elements.isnumeric():
            elements = int(elements)
        new_row.append(elements)
        matrix.append(new_row)
    return matrix


def find_p():

    row_index = 0
    for row in matrix:
        col_index = 0
        for col in row:
            if col == 'P':
                return [row_index, col_index]
            col_index += 1
        row_index += 1


coin = 0
game_over = False
win = False
path = []

def move(movement):
    global coin, game_over, win, player_position
    new_row = 0
    new_col = 0
    if movement == 'up':
        new_row = -1
    if movement == 'down':
        new_row = 1
    if movement == 'left':
        new_col = -1
    if movement == 'right':
        new_col = 1
    if movement not in ['up', 'down', 'left', 'right']:
        return
    new_player_row = player_position[0] + new_row
    new_player_col = player_position[1] + new_col
    if new_player_row < 0 or new_player_row > len(matrix) -1:
        game_over = True
        coin = coin // 2
        return
    if new_player_col < 0 or new_player_col > len(matrix) -1:
        game_over = True
        coin = coin // 2
        return
    if type(matrix[new_player_row][new_player_col]) == int:
        coin += int(matrix[new_player_row][new_player_col])
        matrix[new_player_row][new_player_col] = 0
        path.append('[{}, {}]'.format(new_player_row, new_player_col))
        player_position = [new_player_row, new_player_col]
    if coin >= 100:
        game_over = True
        win = True
        return
    elif matrix[new_player_row][new_player_col] == 'X':
        coin = coin//2
        game_over = True


def read_movement():
    while not game_over:
        mv = input().replace('\n', '')
        move(mv)

matrix = read_matrix()
player_position = find_p()
read_movement()
if win:
    print(f"You won! You've collected {coin} coins.")
else:
    print(f"Game over! You've collected {coin} coins.")
print('Your path: ')
if len(path) > 0:
    for p in path:
        print(p)