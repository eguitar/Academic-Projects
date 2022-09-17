# Eric Trinh / 20091235 / project4.py

import game

class ColumnsGame:
    def __init__(self):
         self._running = True

    def run(self):
        arcade = self._create_board()
        self._setting_field(arcade)

        while self._running:
##            try:
##                print(arcade._faller._faller_status())
##            except: pass
            self._print_board(arcade._board,arcade._status)
##            self._print_board(arcade._status,arcade._status)
            if arcade._matching:
                try:
                    arcade.remove_cells()
                    arcade.drop_cells()
                    arcade.find_match()
                    user = input()
                except game.GameOver:
                    self._running = False
                    print('GAME OVER')
            else:
                self._handles_events(arcade, input())
                if arcade._matching:
                    arcade.find_match()

    def _create_board(self) -> game.Board:
        row = int(input())
        col = int(input())
        arcade = game.Board((col,row))
        return arcade

    def _setting_field(self, arcade: game.Board) -> None:
        mode = input()
        if mode == 'CONTENTS':
            board_field = []
            for row in range(arcade._row):
                user = list(input())
                board_field.append(user)
            for col in range(arcade._col):
                board_column = []
                status_column = []
                for row in range(arcade._row):
                    board_column.append(board_field[row][col])
                    if board_field[row][col] == ' ':
                        status_column.append(0)
                    else:
                        status_column.append(1)
                arcade._board[col] = board_column
                arcade._status[col] = status_column
            arcade._matching = True
            arcade.drop_cells()
            arcade.find_match() 

    def _print_board(self,board: list,status: list):
        for row in range(len(board[0])):
            print('|', end = '')
            for col in range(len(board)):
                if status[col][row] in [0, 1]:
                    chars = [' ',' ']
                elif status[col][row] == 2:
                    chars = ['[',']']
                elif status[col][row] == 3:
                    chars = ['|','|'    ]
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
            arcade.update_falling()
        elif user == '>':
            arcade.shift_faller(1)
            arcade.update_falling()
        elif user == 'Q':
            self._running = False

    
if __name__ == '__main__':
    column_game = ColumnsGame()
    column_game.run()
