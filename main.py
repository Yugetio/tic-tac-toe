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
    if (index > 9 or index < 1 or board[index - 1] in ('x', 'o')):
        return False

    board[index - 1] = player
    return True

def enter_game_step(current_playr):
    index = input('step ' + current_playr  + ': ')

    if index == '0':
        return 0

    if not index.isdigit():
        print('You can enter only integer number!')
        return 0
    elif int(index) < 1 or int(index) > 9:
        print('You can enter only number from 1 to 9!')
        return 0

    return int(index)


def check_win():
    return False
    pass

def start_game():
    current_playr = 'x'
    step = 1
    draw_board()

    while (step <= len(board)):
        index = enter_game_step(current_playr)

        if (index == 0):
            break

        if (game_step(index, current_playr)):
            print('nice')

            draw_board()

            if current_playr == 'x':
                current_playr = 'o'
            else:
                current_playr = 'x'

            step += 1
        else:
            print('incorect step! repeat')


print('start game!')
print('to exit enter 0')
start_game()