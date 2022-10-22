"""
Tests for utils
To moves or rename properly.
"""
from app.src.model.classes.const.color import Color
from app.src.model.classes.const.column import Column
from app.src.model.classes.pieces.bishop import Bishop
from app.src.model.classes.pieces.rook import Rook
from app.src.model.classes.square import Square
from app.src.model.game.board import Board
from app.src.model.miscenaleous.utils import is_square_in_check


def test_is_square_in_check():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | |B| | |
    5 | | | | | | | | |
    4 | | | |X| | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """

    piece_dict = {
        Square(Column.F, 6): Bishop(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    assert is_square_in_check(Color.WHITE, Square(Column.D, 4), board)


def test_is_square_not_in_check():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | |B| | |
    5 | | | | | | | | |
    4 | | | |X| | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.F, 6): Rook(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    assert not is_square_in_check(Color.WHITE, Square(Column.D, 4), board)


def test_is_square_not_in_check2():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | |B| | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.D, 4): Rook(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    assert not is_square_in_check(Color.WHITE, Square(Column.D, 4), board)
