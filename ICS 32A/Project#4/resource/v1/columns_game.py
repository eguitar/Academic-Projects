# Eric Trinh / 20091235 / columns_game.py


class Board:
    def __init__(self):
        self._board = []

    
    def new_board(self, size: tuple):
        self._board = []
        for x in range(size[0]):
            col = []
            for y in range(size[1]):
                col.append('   ')
            self._board.append(col)

    def _create_faller():
        pass
        
    def _fall_faller():
        pass

    def _move_faller():
        pass


class Faller:
    def __init__(self, colors: list):
        self._drop = [f'[{colors[0]}]',f'[{colors[1]}]',f'[{colors[2]}]']

    def rotate(self):
        index = [self._drop[2],self._drop[0],self._drop[1]]
        self._drop = index
        
    def landed(self):
        for i in range(3):
            self._drop[i] = self._drop[i].replace('[','|')
            self._drop[i] = self._drop[i].replace(']','|')

    def floating(self):
        for i in range(3):
            self._drop[i] = self._drop[i].replace('|','[')
            self._drop[i] = self._drop[i].replace('|',']')

    def frozen(self):
        for i in range(3):
            self._drop[i] = self._drop[i].replace('|',' ')
            self._drop[i] = self._drop[i].replace('|',' ')
