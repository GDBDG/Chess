"""
Tests for utils
To moves or rename properly.
"""
from src.CHESS.domain.classes.const.color import Color
from src.CHESS.domain.classes.const.column import Column
from src.CHESS.domain.classes.pieces.bishop import Bishop
from src.CHESS.domain.classes.pieces.rook import Rook
from src.CHESS.domain.classes.square import Square
from src.CHESS.domain.events.event_processor.move_processor import is_square_in_check
from src.CHESS.domain.states.board import Board


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
