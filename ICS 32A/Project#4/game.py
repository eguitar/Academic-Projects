# Eric Trinh / 20091235 / game.py

# statuses:  0 - empty / 1 - frozen / 2 - falling / 3 - landed / 4 - matched

class GameOverInvalidFaller(Exception):
    pass

class GameOverOutOfBound(Exception):
    pass

class GameQuit(Exception):
    pass


class Faller:
    def __init__(self, col: int, jewels: list):
        self._colors = jewels
        self._col = col
        self._rows = [0,1,2]
        self._status = 2
        self._falling = True


class Board:
    def __init__(self, size: tuple):
        self._board = []
        self._status = []
        self._col, self._row = size
        self._faller = None
        self._matching = False

        for col in range(self._col):
            col1, col2 = [], []
            for row in range(self._row+3):
                col1.append(' ')
                col2.append(0)
            self._board.append(col1)
            self._status.append(col2)

    def update_status(self):
        '''Updates the status of the cells by checking
        the position of the faller'''
        self._freeze_faller()
        self._land_faller()
# -------------------------------------------------------------
    def create_faller(self, col: int, colors: list):
        '''Given a column number and list of colors
        creates a faller if one does not exist'''
        if not self._faller_exists():
            self._faller = Faller(col, colors)
            for i in self._faller._rows:
                self._board[self._faller._col][i] = self._faller._colors[i]
                self._status[self._faller._col][i] = self._faller._status
            self.fall_faller()
            self.update_status()

    def rotate_faller(self):
        '''If a faller does not exist, do nothing else, rotates
        the faller such that the top is the bottom, bottom is
        the middle, and the middle is the top'''
        if self._faller_exists():
            index = self._board[self._faller._col][self._faller._rows[-1]]
            self._board[self._faller._col][self._faller._rows[2]] = self._board[self._faller._col][self._faller._rows[1]]
            self._board[self._faller._col][self._faller._rows[1]] = self._board[self._faller._col][self._faller._rows[0]]
            self._board[self._faller._col][self._faller._rows[0]] = index

    def shift_faller(self, num: int):
        '''Given 1 or -1 which corresponds to right or left
        shifts the faller if there are cells available'''
        if self._faller_exists():
            new_col = self._faller._col + num
            if self._valid_shift(new_col):
                for row in self._faller._rows:
                    self._board[new_col][row] = self._board[self._faller._col][row]
                    self._status[new_col][row] = self._status[self._faller._col][row]
                    self._board[self._faller._col][row] = ' '
                    self._status[self._faller._col][row] = 0
                self._faller._col = new_col

    def fall_faller(self):
        '''If a faller exists and it is in the falling state
        moves the faller down one cell'''
        if self._faller_exists() and self._faller._status == 2:
            index = None
            if self._status[self._faller._col][3] == 1:
                self._land_faller()
                return
            for row in reversed(range(self._row+3)):
                if self._status[self._faller._col][row] == 2:
                    if self._valid_cell(self._faller._col,row+1):
                        index = row + 2
                        break
            if self._valid_cell(self._faller._col,index - 1):
                self._board[self._faller._col][index-3:index] = self._board[self._faller._col][index-4:index-1]
                self._status[self._faller._col][index-3:index] = self._status[self._faller._col][index-4:index-1]
                self._board[self._faller._col][index-4] = ' '
                self._status[self._faller._col][index-4] = 0
                for i in range(3):
                    self._faller._rows[i] += 1
# -------------------------------------------------------------
    def remove_cells(self):
        '''Removes all of the matched cells from the board'''
        for col in range(self._col):
            for row in range(self._row+3):
                if self._status[col][row] == 4:
                    self._status[col][row] = 0
                    self._board[col][row] = ' '

    def drop_cells(self):
        '''Iterates through the whole board and drops cells
        down to the bottommost available cell'''
        for col in range(self._col):
            running = True
            while running:
                index = None
                for row in reversed(range(self._row+3)):
                    if self._status[col][row] == 0:
                        index = row + 1
                        break
                if index == None: break
                self._board[col][1:index] = self._board[col][:index-1]
                self._status[col][1:index] = self._status[col][:index-1]
                self._board[col][0],self._status[col][0] = ' ',0
                running = False
                index = None
                for row in reversed(range(self._row+3)):
                    if self._status[col][row] == 0:
                        index = row + 1
                        break
                if index != None:
                    for row in reversed(range(1,index)):
                        if self._status[col][row] != self._status[col][row-1]:
                            running = True
                            
    def find_match(self):
        '''Iterates through every cell to find a list of matching coordates
        for a particular cell, if a list is found, changes the status of
        every cell found to 4 (matched)'''
        matched_points = []
        for col in range(self._col):
            for row in range(self._row+3):
                if self._radial_search(col,row) != []:
                    matched_points.extend(self._radial_search(col,row))
        if matched_points != []:
            for point in matched_points:
                self._status[point[0]][point[1]] = 4
        else:
            self._matching = False
            self.reset_faller()
            self.is_game_over()

    def _radial_search(self, col: int, row: int) -> list:
        '''Given a column and row, searchs for three or more cells matched
        in a row for all eight directions and returns a list containing
        tuples representing the coordinates, empty list is returned if
        none are found'''
        points = []
        if self._linear_search(col,row,1,0) != []:
            points.extend(self._linear_search(col,row,1,0))
        if self._linear_search(col,row,1,1) != []:
            points.extend(self._linear_search(col,row,1,1))
        if self._linear_search(col,row,0,1) != []:
            points.extend(self._linear_search(col,row,0,1))
        if self._linear_search(col,row,-1,1) != []:
            points.extend(self._linear_search(col,row,-1,1))
        if self._linear_search(col,row,-1,0) != []:
            points.extend(self._linear_search(col,row,-1,0))
        if self._linear_search(col,row,-1,-1) != []:
            points.extend(self._linear_search(col,row,-1,-1))
        if self._linear_search(col,row,0,-1) != []:
            points.extend(self._linear_search(col,row,0,-1))
        if self._linear_search(col,row,1,-1) != []:
            points.extend(self._linear_search(col,row,1,-1))
        return points
        
    def _linear_search(self,col: int,row: int,coldelta: int,rowdelta: int) -> list:
        '''Given the coordinates for a cell and the delta components
        returns a list of tuples containing a col and row for each
        cell that is matched, if no cells are matched in the line
        then an empty list is returned'''
        start_cell = self._board[col][row]
        cell_list = []
        if start_cell == ' ':
            return []
        else:
            i = 1
            while True:
                if not self._valid_col(col + coldelta *i) \
                   or not self._valid_row(row + rowdelta *i) \
                   or self._board[col + coldelta *i][row + rowdelta * i] != start_cell:
                    if len(cell_list) < 2:
                        return []
                    else:
                        break
                else: cell_list.append((col + coldelta *i,row + rowdelta * i))
                i += 1
            if len(cell_list) >= 2:
                cell_list.insert(0,(col,row))
                return cell_list
            else: return []
# -------------------------------------------------------------
    def update_falling(self):
        '''Updates the status of the faller when it is shifting'''
        if self._faller_exists():
            self._land_faller()
            if not self._is_faller_land():
                self._set_faller_status(2)
                self._faller._falling = True

    def is_game_over(self):
        '''Checks if a faller is located outside of the board
        and if true, raises GameOver exception'''
        for col in range(self._col):
            if self._board[col][0] != ' ' or self._status[col][0] != 0:
                    raise GameOverInvalidFaller
        for col in range(self._col):
            for row in range(1,3):
                if self._board[col][row] != ' ' or self._status[col][row] != 0:
                    raise GameOverOutOfBound

    def _is_faller_land(self) -> bool:
        '''Returns True is the faller can no longer fall,
        else returns false'''
        if self._faller_exists():
            index = None
            for row in reversed(range(self._row+3)):
                if not self._status[self._faller._col][row] in [0,1,4]:
                    index = row
                    break
            if index == None: return False
            if index == self._row+2 or self._status[self._faller._col][index+1] == 1:
                return True
            else: return False
        else: return False
    
    def _land_faller(self):
        '''Sets the status of the faller to 3 (landed)
        if the faller can no longer fall'''
        if self._is_faller_land():
            self._set_faller_status(3)
            self._faller._falling = False
    
    def _is_faller_freeze(self) -> bool:
        '''Returns True is the faller can no longer fall,
        else returns false'''
        if self._faller_exists():
            if self._faller_status() == 3:
                return True
            else: return False
        else: return False

    def _freeze_faller(self):
        '''Sets the status of the faller to 1 (frozen) if
        the faller can no longer fall and is already landed'''
        if self._is_faller_freeze():
            self._set_faller_status(1)
            self._matching = True
            self.reset_faller()        
# -------------------------------------------------------------
    def reset_faller(self):
        '''Resets the faller to None'''
        self._faller = None
        
    def _set_faller_status(self, status: int):
        '''Given a status number, sets the cells of the
        faller to the corresponding status'''
        for row in self._faller._rows:
            self._status[self._faller._col][row] = status
        self._faller._status = status

    def _faller_status(self) -> int:
        '''Returns the status of the bottommost cell of
        the faller'''
        return self._faller._status

    def _faller_exists(self) -> bool:
        '''Returns whether or not the faller exists
        (False if the faller is equal to None)'''
        if self._faller != None: return True
        else: return False
# -------------------------------------------------------------        
    def _valid_shift(self, col: int) -> bool:
        '''Given a column number, return whether or
        not the cells in that column are available
        for the faller to shift to'''
        if self._valid_col(col):
            for row in self._faller._rows:
                if self._status[col][row] != 0:
                    return False
            return True
        else: return False

    def _valid_cell(self, col: int, row: int) -> bool:
        '''Given a coordinate on the board returns
        whether or not the cell is empty'''
        if not self._valid_col(col) or not self._valid_row(row):
            return False
        if self._status[col][row] == 0: return True
        else: return False

    def _valid_col(self, col: int) -> bool:
        '''Given a column number returns whether or
        not it is a valid column in the board'''
        return (0 <= col and col < self._col)

    def _valid_row(self, row: int) -> bool:
        '''Given a row number returns whether or
        not it is a valid row in the board'''
        return (0 <= row and row < self._row+3)
