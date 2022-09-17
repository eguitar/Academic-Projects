# Eric Trinh / 20091235 / networked_game.py

import connectfour
import game_functions
import network_functions
import sys

if __name__ == '__main__':
    host, port, user = network_functions.user_inputs()
    test, c4 = network_functions.test_connection(host, port)
    if test == False:
        if c4 != None:
            c4.close()
        print('Either the host or port was invalid')
        sys.exit()

    col, row = game_functions.get_col_row()
    game = game_functions.create_game(col, row)

    c4_input, c4_output = network_functions.setup_game(c4, user, col, row)

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
            
        comp_move = network_functions.write_read_move(c4_input, c4_output, move)
        game, test = game_functions.try_move(game, comp_move)
        if test == True:
            sys.exit()
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
    
