board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board_size = 3

mode = None
MODE_PVP = '1'
MODE_PVE = '2'

def draw_board():
    """ малюєм поле """
    print('_' + '_' * 4 * board_size)
    for i in range(board_size):
        print('|' + (' ' * 3 + '|') * 3)
        print('|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
        print('|' + ('_' * 3 + '|') * 3)


def game_step(index: int, player: str):
    if (index < 1 or index > 9 or board[index - 1] in ('x', 'o')):
        return False

    board[index - 1] = player
    return True


def enter_game_step(current_playr: str):
    index = input('step ' + current_playr + ': ')

    if index == '0':
        return 0

    if not index.isdigit():
        print('You can enter only integer number!')
        return 0
    elif int(index) < 1 or int(index) > 9:
        print('You can enter only number from 1 to 9!')
        return 0

    return int(index)


def computer_step(player: str, ai: str):
    # знайти всі доступні шаги
    available_steps = [i - 1 for i in board if type(i) == int]

    # пріорітетність шагів
    win_steps = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    # перебір комбінацій
    for char in (ai, player):
        for pos in available_steps:
            board_ai = board[:]
            board_ai[pos] = char

            if check_win(board_ai):
                return pos

    for pos in win_steps:
        if pos in available_steps:
            return pos

    return -1


def next_player(player: str):
    return 'o' if player == 'x' else 'x'


def check_win(board):
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            return True

    return False


def choose_mode():
    global mode

    while mode not in (MODE_PVP, MODE_PVE):
        mode = input('Choose mode:\n 1 - PvP\n 2 - PvE\nEnter mode: ')


def start_game(mode):
    current_playr = 'x'
    ai_player = 'o'
    step = 1
    draw_board()

    while (step <= len(board)):
        index = enter_game_step(current_playr)

        if (index == 0):
            return 0

        if (game_step(index, current_playr)):
            print('nice')

            draw_board()

            if check_win(board) == True:
                break

            current_playr = next_player(current_playr)

            step += 1

            if mode == MODE_PVE and step <= len(board):
                ai_step = computer_step('x', 'o')
                if ai_step != -1:
                    board[ai_step] = ai_player

                    draw_board()
                    if check_win(board) == True:
                        break

                    current_playr = next_player(current_playr)
                    step += 1

        else:
            print('incorect step! repeat')

    if step == 10:
        print('Draw')
    else:
        print('Winner ' + current_playr)


print('start game!')
print('to exit enter 0')

choose_mode()
start_game(mode)
