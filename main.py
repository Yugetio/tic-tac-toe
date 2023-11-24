import re

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board_size = 3

def draw_board():
    """ малюєм поле """
    print('_' + '_' * 4 * board_size)
    for i in range(board_size):
        print('|' + (' ' * 3 + '|') * 3)
        print('|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
        print('|' + ('_' * 3 + '|') * 3)
    pass

def game_step(index: int, player: str):
    """ виконуємо хід """
    pass

def enter_game_step(current_playr):
    index = input('step ' + current_playr + ' (to exit - 0): ')

    if index == '0':
        return index

    if not index.isdigit():
        print('You can enter only integer number!')
        return '0'
    elif int(index) < 1 or int(index) > 9:
        print('You can enter only number from 1 to 9!')
        return '0'

    return index


def check_win():
    return False
    pass

def start_game():
    current_playr = 'x'
    step = 1
    draw_board()

    while (step <= len(board)):
        index = enter_game_step(current_playr)

        if (index == '0'):
            break

        game_step(index, current_playr)

        step += 1

print('start game!')
start_game()