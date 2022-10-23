"""
Tests for the functions in utils.py
"""
import pytest

from app.src.exceptions.missing_king_error import MissingKingError
from app.src.model.classes.const.color import Color
from app.src.model.classes.const.column import Column
from app.src.model.classes.pieces.bishop import Bishop
from app.src.model.classes.pieces.king import King
from app.src.model.classes.pieces.knight import Knight
from app.src.model.classes.pieces.pawn import Pawn
from app.src.model.classes.pieces.queen import Queen
from app.src.model.classes.pieces.rook import Rook
from app.src.model.classes.square import Square
from app.src.model.states.board import Board


def test_update_config_history():
    """
    Test the method update_config_history
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | |R| | | |
    5 | |P| | | |k| | |
    4 | | | |N| | | | |
    3 | | | | | | | | |
    2 | |Q| | |b| | | |
    1 | | | | | | | | |
       A B C D  E F G H
    @return: None
    """
    piece_dict = {
        Square(Column.D, 4): Knight(Color.WHITE),
        Square(Column.E, 6): Rook(Color.WHITE),
        Square(Column.F, 5): King(Color.BLACK),
        Square(Column.E, 2): Bishop(Color.BLACK),
        Square(Column.B, 5): Pawn(Color.WHITE),
        Square(Column.B, 2): Queen(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    expected_bit_value = 0xD00C00000000000000B000001000E0000002000 << 64
    assert board.dict_to_bit() == expected_bit_value


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


def test_get_piece_type_counter():
    """
    Test get_piece_type_counter
    @return:
    """
    board = Board()
    assert board.get_piece_type_counter() == {
        Bishop: 4,
        King: 2,
        Knight: 4,
        Pawn: 16,
        Queen: 2,
        Rook: 4,
    }


def test_bishop_in_dead_position():
    """
    Test that a dead position with 2 bishops is detected
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | |b| | | | | | |
    3 | | | | |K| |k| |
    2 | |B| | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.B, 2): Bishop(Color.WHITE),
        Square(Column.B, 4): Bishop(Color.BLACK),
        Square(Column.E, 3): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    assert board.are_bishop_in_dead_position()


def test_bishop_not_in_dead_position1():
    """
    Test that a dead position with 2 bishops is detected
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | |b| | |K| |k| |
    2 | |B| | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.B, 2): Bishop(Color.WHITE),
        Square(Column.B, 3): Bishop(Color.BLACK),
        Square(Column.E, 3): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    assert not board.are_bishop_in_dead_position()


def test_bishop_not_in_dead_position2():
    """
    Test that a dead position with 2 bishops is detected
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | |B| | |K| |k| |
    2 | |B| | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.B, 2): Bishop(Color.WHITE),
        Square(Column.B, 3): Bishop(Color.WHITE),
        Square(Column.E, 3): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    assert not board.are_bishop_in_dead_position()


def test_bishop_not_in_dead_position_invalid_position():
    """
    Test that false is returned if there are not 2 bishops and kings.
    @return:
    """
    piece_dict = {
        Square(Column.B, 3): Bishop(Color.WHITE),
        Square(Column.E, 3): King(Color.WHITE),
        Square(Column.G, 3): King(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    assert not board.are_bishop_in_dead_position()
