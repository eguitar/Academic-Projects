# Eric Trinh / 20091235 / project4.py

import game

class ColumnsGame:
    def __init__(self):
         self._running = True

    def run(self):
        arcade = self._create_board()
        self._setting_field(arcade)

        while self._running:
            self._print_board(arcade._board,arcade._status)
            print(arcade.info())
            if not arcade._matching:
                self._handles_events(arcade, input())
                if arcade._matching:
                    arcade.find_match()
            else:
                arcade.remove_cells()
                arcade.drop_cells()
                arcade.find_match()

    def _create_board(self) -> game.Board:
        row = int(input())
        col = int(input())
        arcade = game.Board((col,row))
        return arcade

    def _setting_field(self, arcade: game.Board) -> None:
        mode = input()
        if mode == 'CONTENTS':
            pass #_______________________________________

    def _print_board(self,board: list,status: list):
        for row in range(len(board[0])):
            print('|', end = '')
            for col in range(len(board)):
                if status[col][row] in [0, 1]:
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

    def _handles_events(self, arcade: game.Board, user: str):
        if user == '':
            try:
                arcade.fall_faller()
                arcade.update_status()
            except game.GameOver:
                print(arcade.info())
                self._print_board(arcade._board,arcade._status)
                print('GAME OVER')
                self._running = False
        elif user[0] == 'F':
            try:
                user = user.split(' ')
                arcade.create_faller(int(user[1]),user[2:])
                arcade.fall_faller()
                arcade.update_status()
            except game.GameOver:
                print('GAME OVER')
                self._running = False
        elif user == 'R':
            arcade.rotate_faller()
        elif user == '<':
            arcade.shift_faller(-1)
##            arcade.falling_faller()
        elif user == '>':
            arcade.shift_faller(1)
##            arcade.falling_faller()
        elif user == 'Q':
            self._running = False

    
if __name__ == '__main__':
    column_game = ColumnsGame()
    column_game.run()
