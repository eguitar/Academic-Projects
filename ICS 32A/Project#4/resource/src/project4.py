# Eric Trinh / 20091235 / project4.py

import game

class ColumnsGame:
    def __init__(self):
         self._running = True

    def run(self):
        arcade = self._create_board()
        self._setting_field(arcade)
        self._print_board(arcade)

        while self._running:
            if arcade._matching:
                try:
                    user = input()
                    arcade.remove_cells()
                    arcade.drop_cells()
                    arcade.find_match()                    
                except game.GameOver:
                    self._print_board(arcade)
                    self._running = False
                    print('GAME OVER')
                    break
            else:
                try:
                    self._handles_events(arcade, input())
                    if arcade._matching:
                        try:
                            arcade.find_match()
                        except game.GameOver:
                            self._print_board(arcade)
                            self._running = False
                            print('GAME OVER')
                            break
                except game.GameQuit:
                    self._running = False
                    break
            self._print_board(arcade)


##            self._print_board(arcade)
##            if arcade._matching:
##                try:
##                    arcade.remove_cells()
##                    arcade.drop_cells()
##                    arcade.find_match()
##                    user = input()
##                except game.GameOver:
##                    self._print_board(arcade)
##                    self._running = False
##                    print('GAME OVER')
##            else:
##                self._handles_events(arcade, input())
##                if arcade._matching:
##                    try:
##                        arcade.find_match()
##                    except game.GameOver:
##                        self._print_board(arcade)
##                        self._running = False
##                        print('GAME OVER')

    def _create_board(self) -> game.Board:
        '''Given a row and col number '''
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
                arcade._board[col] = [' ',' ',' ']+board_column
                arcade._status[col] = [0,0,0]+status_column
            arcade._matching = True
            arcade.drop_cells()
            arcade.find_match() 

    def _print_board(self,arcade: game.Board):
        '''Give a board field and status field, prints
        the game showing both the cells and their status'''
        for row in range(3,arcade._row+3):
            print('|', end = '')
            for col in range(arcade._col):
                if arcade._status[col][row] in [0, 1]:
                    chars = [' ',' ']
                elif arcade._status[col][row] == 2:
                    chars = ['[',']']
                elif arcade._status[col][row] == 3:
                    chars = ['|','|'    ]
                elif arcade._status[col][row] == 4:
                    chars = ['*','*']
                print(f'{chars[0]}{arcade._board[col][row]}{chars[1]}',end='')
            print('|')
        print(f" {'---'*arcade._col} ")

    def _handles_events(self, arcade: game.Board, user: str):
        '''Receives user inputs and executes the corresponding
        moves / methods'''
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
                arcade.create_faller(int(user[1])-1,user[2:])
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
            raise game.GameQuit

    
if __name__ == '__main__':
    column_game = ColumnsGame()
    column_game.run()
