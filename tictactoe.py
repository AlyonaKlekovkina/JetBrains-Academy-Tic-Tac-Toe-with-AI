# write your code here
import random


def create_table():
    table = []
    for i in range(3):
        table.append([])
        for j in range(3):
            table[i].append(' ')
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
        elif the_table[column - 1][row - 1] == "X" or the_table[column - 1][row - 1] == "O":
            return 'This cell is occupied! Choose another one!'
        else:
            return int(column), int(row)
    except ValueError:
        return 'You should enter numbers!'


def find_free_slot():
    free_slots = []
    for i in range(3):
        for j in range(3):
            if the_table[i][j] == ' ':
                free_slots.append((i, j))
    return free_slots


def human_plays():
    inp = input('Enter the coordinates: ')
    the_coordinates = get_coordinates(inp)
    while isinstance(the_coordinates, str):
        print(the_coordinates)
        inp = input('Enter the coordinates: ')
        the_coordinates = get_coordinates(inp)
    column, row = the_coordinates
    the_table[column - 1][row - 1] = determine_move(the_table)
    print_board(the_table)


def computer_plays_easy():
    the_slots = find_free_slot()
    if len(the_slots) == 0:
        print('Draw')
    else:
        the_coordinates = random.choice(the_slots)
        print('Making move level "easy"')
        the_table[the_coordinates[0]][the_coordinates[1]] = determine_move(the_table)
        print_board(the_table)


def computer_plays_medium():
    the_slots = find_free_slot()
    if len(the_slots) == 0:
        print('Draw')
    else:
        the_coordinates = random.choice(the_slots)
        print('Making move level "medium"')
        the_table[the_coordinates[0]][the_coordinates[1]] = determine_move(the_table)
        print_board(the_table)


while True:
    inp = input('Input command: ')
    if inp == 'exit':
        break
    else:
        command = [n for n in inp.split()]
        if len(command) != 3:
            print('Bad parameters!')
        else:
            if command[1] == 'easy' and command[2] == 'easy':
                the_table = create_table()
                print_board(the_table)
                for i in range(10):
                    if i % 2 == 0:
                        computer_plays_easy()
                    else:
                        computer_plays_easy()
                    if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
                        print(evaluate_board(the_table))
                        create_table()
                        break
            elif command[1] == 'easy' and command[2] == 'user':
                the_table = create_table()
                print_board(the_table)
                for i in range(10):
                    if i % 2 == 0:
                        computer_plays_easy()
                    else:
                        human_plays()
                    if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
                        print(evaluate_board(the_table))
                        create_table()
                        break
            elif command[1] == 'user' and command[2] == 'easy':
                the_table = create_table()
                print_board(the_table)
                for i in range(10):
                    if i % 2 == 0:
                        human_plays()
                    else:
                        computer_plays_easy()
                    if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
                        print(evaluate_board(the_table))
                        create_table()
                        break
            elif command[1] == 'user' and command[2] == 'user':
                the_table = create_table()
                print_board(the_table)
                for i in range(10):
                    if i % 2 == 0:
                        human_plays()
                    else:
                        human_plays()
                    if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
                        print(evaluate_board(the_table))
                        create_table()
                        break
            elif command[1] == 'user' and command[2] == 'medium':
                the_table = create_table()
                print_board(the_table)
                for i in range(10):
                    if i % 2 == 0:
                        human_plays()
                    else:
                        computer_plays_medium()
                    if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
                        print(evaluate_board(the_table))
                        create_table()
                        break
            elif command[1] == 'medium' and command[2] == 'user':
                the_table = create_table()
                print_board(the_table)
                for i in range(10):
                    if i % 2 == 0:
                        computer_plays_medium()
                    else:
                        human_plays()
                    if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
                        print(evaluate_board(the_table))
                        create_table()
                        break
            elif command[1] == 'medium' and command[2] == 'medium':
                the_table = create_table()
                print_board(the_table)
                for i in range(10):
                    if i % 2 == 0:
                        computer_plays_medium()
                    else:
                        computer_plays_medium()
                    if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
                        print(evaluate_board(the_table))
                        create_table()
                        break
            elif command[1] == 'medium' and command[2] == 'easy':
                the_table = create_table()
                print_board(the_table)
                for i in range(10):
                    if i % 2 == 0:
                        computer_plays_medium()
                    else:
                        computer_plays_easy()
                    if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
                        print(evaluate_board(the_table))
                        create_table()
                        break
            elif command[1] == 'easy' and command[2] == 'medium':
                the_table = create_table()
                print_board(the_table)
                for i in range(10):
                    if i % 2 == 0:
                        computer_plays_easy()
                    else:
                        computer_plays_medium()
                    if evaluate_board(the_table) == 'X wins' or evaluate_board(the_table) == 'O wins' or evaluate_board(the_table) == 'Draw':
                        print(evaluate_board(the_table))
                        create_table()
                        break
