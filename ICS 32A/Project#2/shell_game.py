# Eric Trinh / 20091235 / shell_game.py

import connectfour
import game_functions
import sys

if __name__ == '__main__':
    col, row = game_functions.get_col_row()
    game = game_functions.create_game(col, row)

    while True:
        game, move = game_functions.user_move(game)
        game_functions.print_board(game)
        test = connectfour.winner(game)
        if test == 1:
            print('WINNER_RED')
            break
        elif test == 2:
            print('WINNER_YELLOW')
            break
        if game_functions.stalemate(game):
            sys.exit()
        
