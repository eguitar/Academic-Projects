# Eric Trinh / 20091235 / game.py  

class GameOver(Exception):
    pass


# status (0:empty 1:frozen 2:falling 3:landed 4:matched)

class Board:
    def __init__(self, size: tuple):
        self._board = []
        self._status = []
        self._col,self._row = size
        self._faller = []
        self._faller_col = None
        self._faller_rows = []
        self._matching = False

        for y in range(self._col):
            col1,col2 = [],[]
            for x in range(self._row):
                col1.append(' ')
                col2.append(0)
            self._board.append(col1)
            self._status.append(col2)

    def update_status(self):
        self._freeze_faller()
        self._land_faller()
# -------------------------------------------------------------------------
    def create_faller(self, col: int, colors: list):
        if not self._faller_exists():
            self._faller = colors
            self._faller_col = col - 1

    def rotate_faller(self):
        if not self._faller_exists():
            pass
        elif self._faller == []:
            x = self._faller_rows[2]
            index = self._board[self._faller_col][x]
            for i in reversed(range(1,len(self._faller_rows))):
                f_row = self._faller_rows[i]
                i_row = self._faller_rows[i-1]
                self._board[self._faller_col][f_row] = self._board[self._faller_col][i_row]
            row = self._faller_rows[0]
            self._board[self._faller_col][row] = index
        elif len(self._faller) == 2:
            self._faller.insert(0,self._board[self._faller_col][0])
            self._board[self._faller_col][0] = self._faller.pop()
        else:
            self._faller.insert(0,self._board[self._faller_col][1])
            self._board[self._faller_col][1] = self._board[self._faller_col][0]
            self._board[self._faller_col][0] = self._faller.pop()

    def shift_faller(self, num: int):
        new_col = self._faller_col+num
        if self._valid_shift(new_col):
            for row in self._faller_rows:
                self._board[new_col][row] = self._board[self._faller_col][row]
                self._status[new_col][row] = self._status[self._faller_col][row]
                self._board[self._faller_col][row] = ' '
                self._status[self._faller_col][row] = 0
            self._faller_col = new_col

    def fall_faller(self):
        if self._faller_exists() and not self._is_faller_land():
            self._faller_rows = []
            index = None
            counter = 0
            for i in reversed(range(self._row)):
                if self._status[self._faller_col][i] == 2:
                    index = i + 2
                    break
            if self._status[self._faller_col][0] == 1:
                raise GameOver
            if index == None:
                index = 0
            for i in reversed(range(1,index)):
                if self._valid_fall(self._faller_col,i) and counter != 3:
                    self._board[self._faller_col][i] = self._board[self._faller_col][i-1]
                    self._status[self._faller_col][i] = 2
                    self._faller_rows.insert(0,i)
                    self._board[self._faller_col][i-1] = ' '
                    self._status[self._faller_col][i-1] = 0
                    counter += 1
            if self._valid_fall(self._faller_col,0) and self._faller != []:
                self._board[self._faller_col][0] = self._faller.pop()
                self._status[self._faller_col][0] = 2
                if len(self._faller) in [0,1,2]:
                    self._faller_rows.insert(0,0)
    
##        def falling_faller(self):
##            if self._check_faller_falling():
##                self._set_faller_status(2)
##            else:
##                self._set_faller_status(3)
# -------------------------------------------------------------------------
    def remove_cells(self):
        for col in range(self._col):
            for row in range(self._row):
                if self._status[col][row] == 4:
                    self._status[col][row] = 0
                    self._board[col][row] = ' '
        
    def drop_cells(self):
        for col in range(self._col):
            finished = False
            while not finished:
                index = None
                for row in reversed(range(self._row)):
                    if self._valid_fall(col,row):
                        index = row + 1
                        break
                if index == None: break
                for row in reversed(range(1,index)):
                    self._board[col][row] = self._board[col][row-1]
                    self._status[col][row] = self._status[col][row-1]
                    self._board[col][row-1] = ' '
                    self._status[col][row-1] = 0
                finished = True
                index = None
                for row in reversed(range(self._row)):
                    if self._valid_fall(col,row):
                        index = row + 1
                        break
                if index != None:
                    for row in reversed(range(1,index)):
                        if self._status[col][row] != self._status[col][row-1]:
                            finished = False
# -------------------------------------------------------------------------
    def find_match(self):
        matched_points = []
        for col in range(self._col):
            for row in range(self._row):
                if self._radial_search(col,row) != []:
                    matched_points = self._radial_search(col,row)
                    break
            else:
                continue
            break
        if matched_points != []:
            for point in matched_points:
                self._status[point[0]][point[1]] = 4
        else:
            self._matching = False

    def _radial_search(self, col: int, row: int) -> list:
        points = []
        if self._linear_search(col,row,1,0) != []: points.extend(self._linear_search(col,row,1,0))
        if self._linear_search(col,row,1,1) != []: points.extend(self._linear_search(col,row,1,1))
        if self._linear_search(col,row,0,1) != []: points.extend(self._linear_search(col,row,0,1))
        if self._linear_search(col,row,-1,1) != []: points.extend(self._linear_search(col,row,-1,1))
        if self._linear_search(col,row,-1,0) != []: points.extend(self._linear_search(col,row,-1,0))
        if self._linear_search(col,row,-1,-1) != []: points.extend(self._linear_search(col,row,-1,-1))
        if self._linear_search(col,row,0,-1) != []: points.extend(self._linear_search(col,row,0,-1))
        if self._linear_search(col,row,1,-1) != []: points.extend(self._linear_search(col,row,1,-1))
        else: return points
        
    def _linear_search(self,col: int,row: int,coldelta: int,rowdelta: int) -> list:
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
# -------------------------------------------------------------------------
    def _is_faller_land(self) -> bool:
        if self._faller_exists():
            index = None
            for i in reversed(range(self._row)):
                if not self._status[self._faller_col][i] in [0,1,4]:
                    index = i
                    break
            if index == None: return False
            if index == self._row - 1 or self._status[self._faller_col][index+1] == 1:
                return True
            else:
                return False
        else:
            return False

    def _land_faller(self):
        if self._is_faller_land():
            self._set_faller_status(3)
    
    def _is_faller_freeze(self) -> bool:
        test = True
        if not self._faller_exists() or self._get_faller_status() != 3:
            test = False
        return test

    def _freeze_faller(self):
        if self._is_faller_freeze():
            self._set_faller_status(1)
            if len(self._faller_rows) == 3:
                self._reset_faller()
# -------------------------------------------------------------------------
    def _set_faller_status(self,status: int):
        for row in self._faller_rows:
            self._status[self._faller_col][row] = status

    def _get_faller_status(self) -> int:
        try:
            row = self._faller_rows[-1]
            return self._status[self._faller_col][row]
        except:
            return 0
# -------------------------------------------------------------------------
    def _faller_exists(self) -> bool:
        test = False
        if self._faller != []: test = True           
        if self._faller_col != None: test = True
        if self._faller_rows != []: test = True
        return test

    def _reset_faller(self):
        self._faller = []
        self._faller_col = None
        self._faller_rows = []
        self._matching = True
# -------------------------------------------------------------------------
    def _valid_shift(self,col: int) -> bool:
        if self._valid_col(col):
            test = True
            for row in self._faller_rows:
                if self._status[col][row] != 0:
                    test = False
            return test 
        else:
            return False

    def _valid_fall(self,col: int, row: int) -> bool:
        if self._status[col][row] == 0: return True
        else: return False

    def _valid_col(self, col: int) -> bool:
        return 0 <= col and col < self._col

    def _valid_row(self, row: int) -> bool:
        return 0 <= row and row < self._row

    def info(self):
        print(self._board)
        print(self._status)
        print(self._faller)
        print(self._faller_col)
        print(self._faller_rows)
