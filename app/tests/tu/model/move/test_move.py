"""
Tests for Move class
"""
from app.src.model.available_move_getter.available_moves import (
    get_available_moves,
    is_move_legal,
)
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.move import Move
from app.src.model.move.rook_move import RookMove
from app.src.model.pieces.king import King
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.rook import Rook


def test_is_legal():
    """
    Test that a legal move is detected as legal
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | |W| | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.D, 4): King(Color.WHITE),
        Square(Column.E, 4): Piece(Color.WHITE),
    }
    move = Move(Square(Column.D, 4), Square(Column.C, 3))
    assert is_move_legal(move, piece_dict)


def test_is_not_legal1():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 |K| | | |r| | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.A, 1): King(Color.WHITE),
        Square(Column.E, 1): Rook(Color.BLACK),
    }
    move = Move(Square(Column.A, 1), Square(Column.A, 2))
    assert not is_move_legal(move, piece_dict)


def test_is_not_legal2():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 |K| |Pi||r| | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.A, 1): King(Color.WHITE),
        Square(Column.E, 1): Rook(Color.BLACK),
        Square(Column.C, 1): Piece(Color.WHITE),
    }
    move = Move(Square(Column.C, 1), Square(Column.C, 2))
    assert not is_move_legal(move, piece_dict)


def test_get_move_with_legal_verification():
    """
    Test that get_available moves returns the correct moves
    when legal_verification is True
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 |K| |R| |r| | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.A, 1): King(Color.WHITE),
        Square(Column.E, 1): Rook(Color.BLACK),
        Square(Column.C, 1): Rook(Color.WHITE),
    }
    expected_moves = [
        RookMove(Square(Column.C, 1), Square(Column.D, 1)),
        RookMove(Square(Column.C, 1), Square(Column.E, 1)),
        RookMove(Square(Column.C, 1), Square(Column.B, 1)),
    ]
    assert (
        get_available_moves(Square(Column.C, 1), piece_dict, legal_verification=True)
        == expected_moves
    )
