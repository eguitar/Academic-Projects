# Eric Trinh / 20091235 / project4.py

import columns_game




def ColumnsGame:
    def __init__(self):
        self._game = Board()

        
    def update_board(user: str):
        if user[0] == '':
            pass
        elif user[0] == 'F':
            pass
        elif user[0] == 'R':
            pass
        elif user[0] == '<':
            pass
        elif user[0] == '>':
            pass
        elif user[0] == 'Q':
            pass

    def run() -> None:


    

    
    row, col = _get_game_size()


    



def _get_game_size() -> tuple:
    row = int(input())
    col = int(input())
    return row, col

def _print_board(board: list) -> None:
    for y in range(len(board)):
        print('|',end='')
        for x in range(len(board[0])):
            print(f'{board[y][x]}',end='')
        print('|')
    print(f" {'___'*len(board[0])} ")

if __name__ == '__main__':
    run()
