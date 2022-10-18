"""
Tests for the functions in utils.py
"""
import pytest

from app.src.exceptions.missing_king_error import MissingKingError
from app.src.model.game.board import Board
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
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
    board = Board()
    board.piece_dict = piece_dict
    assert Square(Column.E, 1) == board.get_king(Color.WHITE)
    assert Square(Column.E, 8) == board.get_king(Color.BLACK)


def test_get_king_no_king():
    """
    Test that get_get_king raises an error when there is no king
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    with pytest.raises(MissingKingError):
        board.get_king(Color.BLACK)
