"""
Tests for the pawn moves
"""
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.pawn_move import PawnMove
from app.src.model.pieces.pawn import Pawn


def test_available_squares_forward():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | |B| | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | |W| | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    Test that a pawn can move forward if there is no piece in front of it
    @return:
    """
    piece_dict = {
        Square(Column.E, 3): Pawn(Color.WHITE, ),
        Square(Column.C, 6): Pawn(Color.BLACK, )
    }
    expected_white_move = [PawnMove(Square(Column.E, 3), Square(Column.E, 4))]
    expected_black_move = [PawnMove(Square(Column.C, 6), Square(Column.C, 5))]
    assert (
        PawnMove.get_available_moves(Square(Column.E, 3), piece_dict) == expected_white_move
    )
    assert (
        PawnMove.get_available_moves(Square(Column.C, 6), piece_dict) == expected_black_move
    )
