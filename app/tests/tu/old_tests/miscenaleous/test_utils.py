"""
Tests for the functions in utils.py
"""
import pytest

from app.src.exceptions.missing_king_error import MissingKingError
from app.src.old_model.chess_board.board import Board
from app.src.old_model.miscenaleous.color import Color
from app.src.old_model.miscenaleous.column import Column
from app.src.old_model.miscenaleous.utils import get_king
from app.src.old_model.pieces.king import King


def test_get_king():
    """
    test the method is test_is_king_in_check in check
    when the king is in check
    @return:
    """
    board = Board()
    white_king = board.piece_list[Column.E, 1]
    black_king = board.piece_list[Column.E, 8]
    assert white_king == get_king(board.piece_list, Color.WHITE)
    assert black_king == get_king(board.piece_list, Color.BLACK)


def test_get_king_no_king():
    """
    Test that get_get_king raises an error when there is no king
    @return:
    """
    piece_list = {
        (Column.E, 1): King(Column.E, 1),
    }
    with pytest.raises(MissingKingError):
        get_king(piece_list, Color.BLACK)
