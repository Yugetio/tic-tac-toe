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

def step():
    """ виконуємо хід """
    pass

def check_win():

    pass

def start_game():
    draw_board()
    pass

print('start game!')
start_game()