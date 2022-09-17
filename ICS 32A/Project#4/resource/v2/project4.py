# Eric Trinh / 20091235 / project4.py

import game


class ColumnsGame:
    def __init__(self):
         self._running = True

    def run(self):
        arcade = self._create_board()
        

        while self._running:
            self._print_board(arcade._board,arcade._status)
            self._handles_events(input())

    def _create_board(self) -> game.Board():
        row = int(input())
        col = int(input())
        arcade = game.Board()
        arcade.initialize((col,row))
        return arcade

    def _print_board(self,board: list, status: list):
        for y in range(len(board)):
            print('|',end='')
            for x in range(len(board[0])):
                if status[y][x] == 0:
                    chars = [' ',' ']
                elif status[y][x] == 1:
                    chars = ['[',']']
                elif status[y][x] == 2:
                    chars = ['|','|']
                elif status[y][x] == 3:
                    chars = ['*','*']
                print(f'{chars[0]}{board[y][x]}{chars[1]}',end='')
            print('|')
        print(f" {'___'*len(board[0])} ")

##    def _prints_board(self) -> None:
##        pass

    def _handles_events(self, user: str) -> None:
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
            self._running = False




if __name__ == '__main__':
    column_game = ColumnsGame()
    column_game.run()
