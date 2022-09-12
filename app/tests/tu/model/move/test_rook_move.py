"""
Unit tests for the rook move
"""
from app.src.model.available_move_getter.available_moves import get_available_moves
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.rook_move import RookMove
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.rook import Rook


def test_available_moves():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | |W| | | | |
    5 | | | | | | | | |
    4 | | | |W| | |B| |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.D, 4): Rook(Color.WHITE),
        Square(Column.D, 6): Piece(Color.WHITE),
        Square(Column.G, 4): Piece(Color.BLACK),
    }
    expected_moves = [
        RookMove(Square(Column.D, 4), Square(Column.E, 4)),
        RookMove(Square(Column.D, 4), Square(Column.F, 4)),
        RookMove(Square(Column.D, 4), Square(Column.G, 4)),
        RookMove(Square(Column.D, 4), Square(Column.C, 4)),
        RookMove(Square(Column.D, 4), Square(Column.B, 4)),
        RookMove(Square(Column.D, 4), Square(Column.A, 4)),
        RookMove(Square(Column.D, 4), Square(Column.D, 5)),
        RookMove(Square(Column.D, 4), Square(Column.D, 3)),
        RookMove(Square(Column.D, 4), Square(Column.D, 2)),
        RookMove(Square(Column.D, 4), Square(Column.D, 1)),
    ]
    assert (
        get_available_moves(Square(Column.D, 4), piece_dict) == expected_moves
    )
