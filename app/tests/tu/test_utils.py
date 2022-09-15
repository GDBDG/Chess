"""
Tests for the functions in utils.py
"""
import pytest

from app.src.exceptions.missing_king_error import MissingKingError
from app.src.model.available_move_getter.is_square_in_check import is_square_in_check
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.utils import get_king
from app.src.model.pieces.bishop import Bishop
from app.src.model.pieces.king import King
from app.src.model.pieces.rook import Rook


def test_get_king():
    """
    test the method is test_is_king_in_check in check
    when the king is in check
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.E, 8): King(Color.BLACK),
    }
    assert Square(Column.E, 1) == get_king(piece_dict, Color.WHITE)
    assert Square(Column.E, 8) == get_king(piece_dict, Color.BLACK)


def test_get_king_no_king():
    """
    Test that get_get_king raises an error when there is no king
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
    }
    with pytest.raises(MissingKingError):
        get_king(piece_dict, Color.BLACK)


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
    assert is_square_in_check(Color.WHITE, Square(Column.D, 4), piece_dict)


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
    assert not is_square_in_check(Color.WHITE, Square(Column.D, 4), piece_dict)


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
    assert not is_square_in_check(Color.WHITE, Square(Column.D, 4), piece_dict)
