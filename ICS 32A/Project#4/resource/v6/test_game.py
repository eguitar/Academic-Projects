# Eric Trinh / 20091235 / test_game.py

import game
import unittest

class ColumnsGameTest(unittest.TestCase):
    def setUp(self):
        self._game = game.Board((4,5))

    # FALL METHOD
    def test_fall_no_faller(self):
        self._game.fall_faller()
        self.assertEqual(self._game._board,
                         [[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_fall_one_cell_into_board(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self.assertEqual(self._game._board,
                         [['V',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_fall_two_cells_into_board(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self.assertEqual(self._game._board,
                         [['T','V',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,2,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_fall_three_cells_into_board(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self.assertEqual(self._game._board,
                         [['S','T','V',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,2,2,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_fall_cells_in_board(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self.assertEqual(self._game._board,
                         [[' ','S','T','V',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,2,2,2,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    # ROTATE METHOD
    def test_rotate_no_faller(self):
        self._game.rotate_faller()
        self.assertEqual(self._game._board,
                         [[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_rotate_faller_one_cell_in_board(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.rotate_faller()
        self.assertEqual(self._game._board,
                         [['T',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        

    def test_rotate_faller_two_cells_in_board(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.rotate_faller()
        self.assertEqual(self._game._board,
                         [['S','T',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,2,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_rotate_faller_three_cells_in_board(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.rotate_faller()
        self.assertEqual(self._game._board,
                         [['V','S','T',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,2,2,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_rotate_faller_after_shifting_faller(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.shift_faller(1)
        self._game.rotate_faller()
        self.assertEqual(self._game._board,
                         [[' ',' ',' ',' ',' '],['V','S','T',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,0,0,0],[2,2,2,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_rotate_faller_after_faller_landed(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.update_status()
        self._game.rotate_faller()
        self.assertEqual(self._game._board,
                         [[' ',' ','V','S','T'],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,3,3,3],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        

    def test_rotate_faller_after_faller_frozen(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.update_status()
        self._game.update_status()
        self._game.reset_faller()
        self._game.rotate_faller()
        self.assertEqual(self._game._board,
                         [[' ',' ','S','T','V'],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    # SHIFT METHOD
    def test_shift_faller_out_board(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.shift_faller(-1)
        self.assertEqual(self._game._board,
                         [['S','T','V',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,2,2,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_shift_faller_in_board(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.shift_faller(1)
        self.assertEqual(self._game._board,
                         [[' ',' ',' ',' ',' '],['S','T','V',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,0,0,0],[2,2,2,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_shift_faller_onto_frozen_cell(self):
        self._game._board = [[' ',' ',' ',' ',' '],[' ',' ','S','T','V'],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
        self._game._status = [[0,0,0,0,0],[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,0]]
        
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.shift_faller(1)
        self._game.update_falling()
        self.assertEqual(self._game._board,
                         [[' ',' ',' ',' ',' '],['T','V','S','T','V'],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,0,0,0],[3,3,1,1,1],[0,0,0,0,0],[0,0,0,0,0]])

    def test_shift_faller_onto_empty_cell(self):
        self._game._board = [[' ',' ',' ',' ',' '],[' ',' ','S','T','V'],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']]
        self._game._status = [[0,0,0,0,0],[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,0]]
        
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.fall_faller()
        self._game.shift_faller(1)
        self._game.update_falling()
        self._game.shift_faller(-1)
        self._game.update_falling()
        self.assertEqual(self._game._board,
                         [['T','V',' ',' ',' '],[' ',' ','S','T','V'],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,2,0,0,0],[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,0]])
    # REMOVE METHOD
    def test_remove_cells_matched_basic(self):
        self._game._board = [[' ',' ','S','T','X'],[' ',' ',' ','X','X'],[' ',' ','X','Y','X'],[' ',' ','X','S','X']]
        self._game._status = [[0,0,1,1,4],[0,0,0,4,4],[0,0,4,1,4],[0,0,1,1,4]]
        self._game.remove_cells()
        self.assertEqual(self._game._board,
                         [[' ',' ','S','T',' '],[' ',' ',' ',' ',' '],[' ',' ',' ','Y',' '],[' ',' ','X','S',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,1,1,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,0]])
        
    def test_remove_nothing_to_remove(self):
        self._game._board = [[' ','X','S','Y','V'],['R','X','S','T','V'],[' ',' ',' ',' ','Y'],['T','Y','Y','Y','Y']]
        self._game._status = [[0,1,1,1,1],[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1]]
        self._game.remove_cells()
        self.assertEqual(self._game._board,
                         [[' ','X','S','Y','V'],['R','X','S','T','V'],[' ',' ',' ',' ','Y'],['T','Y','Y','Y','Y']])
        self.assertEqual(self._game._status,
                         [[0,1,1,1,1],[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1]])
    # DROP METHOD
    def test_drop_matched_removed_basic(self):
        self._game._board = [[' ','X',' ','Y',' '],['R',' ','S','T','V'],['X',' ','Y',' ','Y'],['T','Y','Y','Y','Y']]
        self._game._status = [[0,1,0,1,0],[1,0,1,1,1],[1,0,1,0,1],[1,1,1,1,1]]
        self._game.drop_cells()
        self.assertEqual(self._game._board,
                         [[' ',' ',' ','X','Y'],[' ','R','S','T','V'],[' ',' ','X','Y','Y'],['T','Y','Y','Y','Y']])
        self.assertEqual(self._game._status,
                         [[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1],[1,1,1,1,1]])

    def test_drop_nothing_to_drop(self):
        self._game._board = [[' ','X','S','Y','V'],['R','X','S','T','V'],[' ',' ',' ',' ','Y'],['T','Y','Y','Y','Y']]
        self._game._status = [[0,1,1,1,1],[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1]]
        self._game.drop_cells()
        self.assertEqual(self._game._board,
                         [[' ','X','S','Y','V'],['R','X','S','T','V'],[' ',' ',' ',' ','Y'],['T','Y','Y','Y','Y']])
        self.assertEqual(self._game._status,
                         [[0,1,1,1,1],[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1]])
    # FIND MATCH METHOD
    def test_match_multiple_instances(self):
        self._game._board = [[' ',' ','S','T','X'],[' ',' ','T','X','X'],[' ','T','X','Y','X'],[' ',' ','X','S','X']]
        self._game._status = [[0,0,1,1,1],[0,0,1,1,1],[0,1,1,1,1],[0,0,1,1,1]]
        self._game.find_match()
        self.assertEqual(self._game._board,
                         [[' ',' ','S','T','X'],[' ',' ','T','X','X'],[' ','T','X','Y','X'],[' ',' ','X','S','X']])
        self.assertEqual(self._game._status,
                         [[0,0,1,4,4],[0,0,4,4,4],[0,4,4,1,4],[0,0,1,1,4]])

    def test_match_nothing_to_match(self):
        self._game._board = [[' ',' ','Y','T','X'],[' ',' ','T','Z','Z'],[' ','S','X','Y','X'],[' ',' ','X','S','X']]
        self._game._status = [[0,0,1,1,1],[0,0,1,1,1],[0,1,1,1,1],[0,0,1,1,1]]
        self._game.find_match()
        self.assertEqual(self._game._board,
                         [[' ',' ','Y','T','X'],[' ',' ','T','Z','Z'],[' ','S','X','Y','X'],[' ',' ','X','S','X']])
        self.assertEqual(self._game._status,
                         [[0,0,1,1,1],[0,0,1,1,1],[0,1,1,1,1],[0,0,1,1,1]])
    # UPDATE STATUS METHOD
    def test_update_status_still_falling(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.update_status()
        self.assertEqual(self._game._board,
                         [['V',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        self._game.fall_faller()
        self._game.update_status()
        self.assertEqual(self._game._board,
                         [['T','V',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,2,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        self._game.fall_faller()
        self._game.update_status()
        self.assertEqual(self._game._board,
                         [['S','T','V',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[2,2,2,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_update_status_faller_landed(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.update_status()
        self._game.fall_faller()
        self._game.update_status()
        self._game.fall_faller()
        self._game.update_status()
        self._game.fall_faller()
        self._game.update_status()
        self._game.fall_faller()
        self._game.update_status()
        self.assertEqual(self._game._board,
                         [[' ',' ','S','T','V'],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,3,3,3],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_update_status_faller_frozen(self):
        self._game.create_faller(1, ['S','T','V'])
        self._game.fall_faller()
        self._game.update_status()
        self._game.fall_faller()
        self._game.update_status()
        self._game.fall_faller()
        self._game.update_status()
        self._game.fall_faller()
        self._game.update_status()
        self._game.fall_faller()
        self._game.update_status()
        self._game.update_status()
        self.assertEqual(self._game._board,
                         [[' ',' ','S','T','V'],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']])
        self.assertEqual(self._game._status,
                         [[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])


if __name__ == '__main__':
    unittest.main()
