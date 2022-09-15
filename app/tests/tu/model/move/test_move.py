"""
Tests for Move class
"""
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.move import Move
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
    assert move.is_legal(piece_dict)


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
    assert not move.is_legal(piece_dict)


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
    assert not move.is_legal(piece_dict)
