# Eric Trinh / 20091235 / game_functions.py

import connectfour

def get_col_row() -> (int, int):
    '''
    Prompts the user to input two values for the column and row
    of the board. If the input is not in between 1 and 20 inclusive
    or is not an integer, then the user is notified and asked again.
    '''
    p1 = 'Enter an integer between 1 and 20 inclusive for the # of column(s)\n'
    p2 = 'Enter an integer between 1 and 20 inclusive for the # of row(s)\n'
    while True:
        try:
            col = int(input(p1))
        except:
            print('Invalid input')
        else:
            if col in range(1,21):
                break
            else:
                print('Invalid input')
    while True:
        try:
            row = int(input(p2))
        except:
            print('Invalid input')
        else:
            if row in range(1,21):
                break
            else:
                print('Invalid input')

    return col, row


def create_game(col: int, row: int) -> connectfour.GameState:
    '''
    Given two integers corresponding to the number of columns
    and rows, returns a game state and prints the initial board
    '''
    game = connectfour.new_game(col, row)
    print_board(game)

    return game


def print_board(game: connectfour.GameState) -> None:
    '''
    Given a game state, prints the current board
    '''
    for col in range(1, connectfour.columns(game) + 1):
        if col in range(1,9) and col != connectfour.columns(game):
            spacer = '  '
        elif col == connectfour.columns(game):
            spacer = '\n'
        else:
            spacer = ' '
        print(f'{col}{spacer}', end = '')
    for row in range(connectfour.rows(game)):
        for col in range(connectfour.columns(game)):
            if col == connectfour.columns(game) - 1:
                spacer = '\n'
            else:
                spacer = '  '
            slot = '.'
            if game.board[col][row] == 1:
                slot = 'R'
            elif game.board[col][row] == 2:
                slot = 'Y'
            print(f'{slot}{spacer}',end='')


def stalemate(game: connectfour.GameState) -> bool:
    '''
    Gven a game state tests to see if there are any
    possible moves left, if there aren't returns True
    '''
    bottom = []
    row = connectfour.rows(game)-1
    for col in range(connectfour.columns(game)):
        bottom.append(game.board[col][row])
    empty = True
    for col in range(connectfour.columns(game)):
        if game.board[col][0] == 0:
            empty = False
    if (not game.turn in bottom) and empty:
        print('STALEMATE')
        return True
    else:
        return False


def user_move(game: connectfour.GameState) -> (connectfour.GameState, [str]):
    '''
    Given a game state, prompts the user to make a move. Once a
    valid move is inputted and successfully applied, returns a
    new game state and the move's two parts in a list. If the
    move is invalid, continues to prompt the user until a valid
    one is entered.
    '''
    prompt = '''To make a move, enter DROP or POP followed
by a space and an integer corresponding to
the column with 1 being the leftmost
(Ex. DROP 5 | POP 3)\n'''
    index = True
    while index:
        move = input(prompt).split()
        next_game, index = try_move(game,move)

    return next_game, move

def try_move(game: connectfour.GameState, move: [str]) -> (connectfour.GameState, bool):
    ''' 
    Given a game state and a list of strings, attempts to make the
    move. If the move is valid, a new game state is return as well
    as an index of False in order to exit out of loops
    '''
    g = None
    try:
        if move[0] == 'DROP' and len(move) == 2:
            g = connectfour.drop(game, int(move[1]) - 1)
            index = False
        elif move[0] == 'POP' and len(move) == 2:
            g = connectfour.pop(game, int(move[1]) - 1)
            index = False
        else:
            raise ValueError
    except:
        print('INVALID')
        index = True

    return g, index


