# Eric Trinh / 20091235 / game.py  


class Board:
    def __init__(self):
        self._board = []
        self._status = []  # status (0:frozen 1:falling 2:landed 3:matched)
        self._faller = []
        self._faller_col = None
        self._faller_points = []

    def initialize(self, size: tuple):
        for x in range(size[0]):
            col = []
            for y in range(size[1]):
                col.append(' ')
            self._board.append(col)
        for x in range(size[0]):
            col = []
            for y in range(size[1]):
                col.append(0)
            self._status.append(col)

    def create_faller(self, col: int, colors: list):
        if self._faller == [] and self._faller_col == None:
            self._faller = colors
            self._faller_col = col - 1
            self.fall_faller()
            
    def fall_faller(self):
        index = None
        for i in reversed(range(len(self._board[0]))):
            if self._status[self._faller_col][i] == 1:
                index = i + 2
                break
        if index == None:
            index = 0
        counter = 0
        for i in reversed(range(index)):
            if self._cell_available(self._faller_col,i) and counter != 3:
                try:
                    self._board[self._faller_col][i] = self._board[self._faller_col][i-1]
                    self._status[self._faller_col][i] = 1
                    self._board[self._faller_col][i-1] = ' '
                    self._status[self._faller_col][i-1] = 0
                    counter += 1
                except:
                    pass
        
        if self._cell_available(self._faller_col,0) and self._faller != []:
            self._board[self._faller_col][0] = self._faller.pop()
            self._status[self._faller_col][0] = 1
        

    def move_faller(self):
        pass

    def rotate_faller(self):
        pass

    def _cell_available(self,col: int, row: int) -> bool:
        if self._board[col][row] == ' ':
            return True
        else:
            return False


x = Board()
x.initialize((3,6))
x.create_faller(2, ['S','T','V'])
x._faller
x._faller_col
x.fall_faller()
