"""
Tests for the functions in utils.py
"""
import pytest

from app.src.exceptions.missing_king_error import MissingKingError
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.utils import get_king
from app.src.model.pieces.king import King


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
