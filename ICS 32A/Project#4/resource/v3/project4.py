# Eric Trinh / 20091235 / project4.py

import game


class ColumnsGame:
    def __init__(self):
         self._running = True

    def run(self):
        arcade = self._create_board()

        while self._running:
##            try:
                self._print_board(arcade._board,arcade._status)
                self._handles_events(arcade, input())
##            except:
##                self._running = False

    def _create_board(self) -> game.Board:
        row = int(input())
        col = int(input())
        mode = input()
        arcade = game.Board((col,row))
        if mode == 'EMPTY':
            return arcade
        elif mode == 'CONTENTS':
            pass #____________________________________
                

    def _print_board(self,board: list, status: list):
        for row in range(len(board[0])):
            print('|',end='')
            for col in range(len(board)):
                if status[col][row] == 0 or status[col][arrow] == 1:
                    chars = [' ',' ']
                elif status[col][row] == 2:
                    chars = ['[',']']
                elif status[col][row] == 3:
                    chars = ['|','|']
                elif status[col][row] == 4:
                    chars = ['*','*']
                print(f'{chars[0]}{board[col][row]}{chars[1]}',end='')
            print('|')
        print(f" {'---'*len(board)} ")

    def _handles_events(self, arcade: game.Board, user: str) -> None:
        if user == '':
            arcade.update_board()
        elif user[0] == 'F':
            user = user.split(' ')
            arcade.create_faller(int(user[1]),user[2:])
            arcade.update_board()
        elif user == 'R':
            arcade.rotate_faller()
        elif user == '<':
            arcade.move_faller(-1)
        elif user == '>':
            arcade.move_faller(1)
        elif user == 'Q':
            self._running = False

if __name__ == '__main__':
    column_game = ColumnsGame()
    column_game.run()
