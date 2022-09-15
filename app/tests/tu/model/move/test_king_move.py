"""
Tests for the king basic moves
"""

from app.src.model.available_move_getter.available_moves import get_available_moves
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.king_move import KingMove
from app.src.model.pieces.king import King
from app.src.model.pieces.piece import Piece


def test_available_king_moves():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | |W|W| | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    No need to do extensive tests, since they are done in the Piece tests
    (The rook moves uses _available_square_on_side_line, already completely
    tested)
    @return:
    """
    piece_dict = {
        Square(Column.D, 4): King(Color.WHITE),
        Square(Column.E, 4): Piece(Color.WHITE),
    }
    expected_moves = [
        KingMove(Square(Column.D, 4), Square(Column.C, 3)),
        KingMove(Square(Column.D, 4), Square(Column.C, 4)),
        KingMove(Square(Column.D, 4), Square(Column.C, 5)),
        KingMove(Square(Column.D, 4), Square(Column.D, 3)),
        KingMove(Square(Column.D, 4), Square(Column.D, 5)),
        KingMove(Square(Column.D, 4), Square(Column.E, 3)),
        KingMove(Square(Column.D, 4), Square(Column.E, 5)),
    ]
    assert get_available_moves(Square(Column.D, 4), piece_dict) == expected_moves


def test_available_king_moves_2_kings():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 |W| | | |B| | | |
       A B C D E F G H
    Test the infinite loop with 2 kings
    @return:
    """
    piece_dict = {
        Square(Column.A, 1): King(Color.WHITE),
        Square(Column.E, 1): King(Color.BLACK),
    }
    expected_moves = [
        KingMove(Square(Column.A, 1), Square(Column.A, 2)),
        KingMove(Square(Column.A, 1), Square(Column.B, 1)),
        KingMove(Square(Column.A, 1), Square(Column.B, 2)),
    ]
    assert get_available_moves(Square(Column.A, 1), piece_dict) == expected_moves
