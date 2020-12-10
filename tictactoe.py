# write your code here


def fill_table_from_input(table_state):
    table = []
    k = 0
    for i in range(3):
        table.append([])
        for j in range(3):
            if table_state[k + j] == '_':
                table[i].append(' ')
            else:
                table[i].append(table_state[k + j])
        k += 3
    return table


def print_board(table):
    print('---------')
    for r in table:
        print('|', *r, '|')
    print('---------')


def evaluate_board(table):
    # evaluating rows and checks if there is a draw
    board = 0
    for i in range(3):
        count_x = 0
        count_o = 0
        for j in range(3):
            if table[i][j] == 'X':
                count_x += 1
                board += 1
                if count_x == 3:
                    return 'X wins'
            if table[i][j] == 'O':
                count_o += 1
                board += 1
                if count_o == 3:
                    return 'O wins'
            elif board == 9:
                return 'Draw'
    # evaluating columns
    for i in range(3):
        col_x = 0
        col_o = 0
        for j in range(3):
            if table[j][i] == 'X':
                col_x += 1
                if col_x == 3:
                    return 'X wins'
            if table[j][i] == 'O':
                col_o += 1
                if col_o == 3:
                    return 'O wins'
    # evaluating diagonals
    if table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X':
        return 'X wins'
    if table[0][2] == 'X' and table[1][1] == 'X' and table[2][0] == 'X':
        return 'X wins'
    if table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O':
        return 'O wins'
    if table[0][2] == 'O' and table[1][1] == 'O' and table[2][0] == 'O':
        return 'O wins'


def determine_move(table):
    num_of_x = 0
    num_of_o = 0
    for i in range(3):
        for j in range(3):
            if table[i][j] == 'X':
                num_of_x += 1
            if table[i][j] == 'O':
                num_of_o += 1
    if num_of_x <= num_of_o:
        return 'X'
    else:
        return 'O'


def get_coordinates(input_coordinates):
    try:
        column, row = input_coordinates.split()
        column, row = int(column), int(row)
        if (column < 1) or (column > 3) or (row < 1) or (row > 3):
            return 'Coordinates should be from 1 to 3!'
        elif the_table[3 - row][column - 1] == "X" or the_table[3 - row][column - 1] == "O":
            return 'This cell is occupied! Choose another one!'
        else:
            return int(column), int(row)
    except ValueError:
        return 'You should enter numbers!'


the_table = fill_table_from_input(input('Enter the cells: '))
print_board(the_table)

inp = input('Enter the coordinates: ')
the_coordinates = get_coordinates(inp)
while isinstance(the_coordinates, str):
    print(the_coordinates)
    inp = input('Enter the coordinates: ')
    the_coordinates = get_coordinates(inp)

column, row = the_coordinates
the_table[3 - row][column - 1] = determine_move(the_table)
print_board(the_table)
if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
    print(evaluate_board(the_table))
else:
    print('Game not finished')
