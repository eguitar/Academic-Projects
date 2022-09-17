# Eric Trinh / 20091235 / game.py  

class Board:
    def __init__(self, size: tuple):
        self._board = []
        self._status = []
        # status (0:empty 1:frozen 2:falling 3:landed 4:matched)
        self._faller = []
        self._faller_col = None
        self._faller_rows = []

        for x in range(size[0]):
            col1,col2 = [],[]
            for y in range(size[1]):
                col1.append(' ')
                col2.append(0)
            self._board.append(col1)
            self._status.append(col2)
            
    def create_faller(self, col: int, colors: list):
        if self._faller == [] and self._faller_col == None:
            self._faller = colors
            self._faller_col = col - 1
            
    def update_board(self):
        if self._check_faller_freeze():
            self._freeze_faller()
        elif self._check_faller_land():
            self._land_faller()
        else:
            self._fall_faller()
            if self._check_faller_land():
                self._land_faller()

    def rotate_faller(self):
        if self._faller == []:
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
    
    def move_faller(self, num: int):
        new_col = self._faller_col+num
        if self._column_available(new_col):
            for point in self._faller_rows:
                self._board[new_col][point] = self._board[self._faller_col][point]
                self._status[new_col][point] = self._status[self._faller_col][point]
                self._board[self._faller_col][point] = ' '
                self._status[self._faller_col][point] = 0
            self._faller_col = new_col

    def _fall_faller(self):
        try:
            self._faller_rows = []
            index = None
            counter = 0
            for i in reversed(range(len(self._board[0]))):
                if self._status[self._faller_col][i] == 2:
                    index = i + 2
                    break
            if index == None:
                index = 0        
            for i in reversed(range(index)):
                if self._cell_below_available(self._faller_col,i) and counter != 3:
                    self._board[self._faller_col][i] = self._board[self._faller_col][i-1]
                    self._status[self._faller_col][i] = 2
                    self._faller_rows.insert(0,i)
                    self._board[self._faller_col][i-1] = ' '
                    self._status[self._faller_col][i-1] = 0
                    counter += 1
            if self._cell_below_available(self._faller_col,0) and self._faller != []:
                self._board[self._faller_col][0] = self._faller.pop()
                self._status[self._faller_col][0] = 2
                if len(self._faller) == 2:
                    self._faller_rows.insert(0,0)
        except:
            pass

    def _check_faller_land(self) -> bool:
        index = None
        for i in reversed(range(len(self._board[0]))):
            if self._status[self._faller_col][i] == 2:
                index = i
                break
        if index == None: return False
        if index == len(self._board[0]) - 1 or self._status[self._faller_col][index+1] == 1:
            return True
        else:
            return False

    def _land_faller(self):
        for point in self._faller_rows:
            self._status[self._faller_col][point] = 3
    
    def _check_faller_freeze(self) -> bool:
        test = False
        for point in self._faller_rows:
            if self._status[self._faller_col][point] == 3:
                test = True
            else:
                test = False
        return test

    def _freeze_faller(self):
        for point in self._faller_rows:
            self._status[self._faller_col][point] = 1
        self._reset_faller()

    def _column_available(self,col: int) -> bool:
        if col in range(len(self._board)):
            test = True
            for point in self._faller_rows:
                if self._status[col][point] != 0:
                    test = False
            return test 
        else:
            return False

    def _cell_below_available(self,col: int, row: int) -> bool:
        if self._board[col][row] == ' ': return True
        else: return False
        
    def _reset_faller(self):
        self._faller = []
        self._faller_col = None
        self._faller_rows = []

    def info(self):
        print(self._board)
        print(self._status)
        print(self._faller)
        print(self._faller_col)
        print(self._faller_rows)
        
x = Board((3,6))
x.create_faller(1, ['S','T','V'])
