"""
Tests for the pawn moves
"""
from app.src.model.available_move_getter.available_moves import get_available_moves
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.knight_promotion import KnightPromotion
from app.src.model.move.pawn_move import PawnMove
from app.src.model.move.queen_promotion import QueenPromotion
from app.src.model.pieces.pawn import Pawn


def test_available_move_square_forward():
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
        Square(Column.E, 3): Pawn(
            Color.WHITE,
        ),
        Square(Column.C, 6): Pawn(
            Color.BLACK,
        ),
    }
    expected_white_move = [PawnMove(Square(Column.E, 3), Square(Column.E, 4))]
    expected_black_move = [PawnMove(Square(Column.C, 6), Square(Column.C, 5))]
    assert (
        get_available_moves(Square(Column.E, 3), piece_dict)
        == expected_white_move
    )
    assert (
        get_available_moves(Square(Column.C, 6), piece_dict)
        == expected_black_move
    )


def test_available_move_promotion():
    """
    8 | | | | | | | | |
    7 | | | | |W| | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | |B| | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    Test that a pawn can move forward if there is no piece in front of it
    @return:
    """
    piece_dict = {
        Square(Column.E, 7): Pawn(Color.WHITE),
        Square(Column.C, 2): Pawn(Color.BLACK),
    }
    expected_white_move = [
        QueenPromotion(Square(Column.E, 7), Square(Column.E, 8)),
        KnightPromotion(Square(Column.E, 7), Square(Column.E, 8)),
    ]
    expected_black_move = [
        QueenPromotion(Square(Column.C, 2), Square(Column.C, 1)),
        KnightPromotion(Square(Column.C, 2), Square(Column.C, 1)),
    ]
    assert (
        get_available_moves(Square(Column.E, 7), piece_dict)
        == expected_white_move
    )
    assert (
        get_available_moves(Square(Column.C, 2), piece_dict)
        == expected_black_move
    )
