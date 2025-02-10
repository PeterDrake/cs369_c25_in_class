from tictactoe import *

def test_finds_successor():
    assert successor(INITIAL_STATE, 1, 'X') == '.X.......'

def test_finds_legal_moves():
    assert legal_moves('.X...O...') == [0, 2, 3, 4, 6, 7, 8]

def test_finds_win_for_x():
    assert winner('...XXX.OO') == 1

def test_finds_win_for_o():
    assert winner('...XX.OOO') == -1
