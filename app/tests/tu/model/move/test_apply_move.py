"""
Tests move application
"""
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.knight_promotion import KnightPromotion
from app.src.model.move.knight_promotion_capture import KnightPromotionCapture
from app.src.model.move.move import Move
from app.src.model.move.queen_promotion import QueenPromotion
from app.src.model.move.queen_promotion_capture import QueenPromotionCapture
from app.src.model.pieces.knight import Knight
from app.src.model.pieces.pawn import Pawn
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.queen import Queen


def test_apply_move_no_capture():
    """
    Test that a move is applied
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | |W| | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.E, 2): Piece(Color.WHITE),
    }
    move = Move(Square(Column.E, 2), Square(Column.E, 4))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.E, 4)] == Piece(Color.WHITE)
    assert Square(Column.E, 2) not in piece_dict
    assert not capture


def test_apply_move_capture():
    """
    Test that a move is applied
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | |B| | | |
    3 | | | | | | | | |
    2 | | | | |W| | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.E, 2): Piece(Color.WHITE),
        Square(Column.E, 4): Piece(Color.BLACK),
    }
    move = Move(Square(Column.E, 2), Square(Column.E, 4))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.E, 4)] == Piece(Color.WHITE)
    assert Square(Column.E, 2) not in piece_dict
    assert capture


def test_apply_knight_promotion():
    """
    Test a knight promotion
    8 | | | | | | | | |
    7 | | | | |W| | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | |B| | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.E, 7): Pawn(Color.WHITE),
        Square(Column.E, 2): Pawn(Color.BLACK),
    }
    move = KnightPromotion(Square(Column.E, 7), Square(Column.E, 8))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.E, 8)] == Knight(Color.WHITE)
    assert Square(Column.E, 7) not in piece_dict
    assert not capture

    move = KnightPromotion(Square(Column.E, 2), Square(Column.E, 1))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.E, 1)] == Knight(Color.BLACK)
    assert Square(Column.E, 2) not in piece_dict
    assert not capture


def test_apply_queen_promotion():
    """
    Test a knight promotion
    8 | | | | | | | | |
    7 | | | | |W| | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | |B| | | |
    1 | | | | | | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.E, 7): Pawn(Color.WHITE),
        Square(Column.E, 2): Pawn(Color.BLACK),
    }
    move = QueenPromotion(Square(Column.E, 7), Square(Column.E, 8))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.E, 8)] == Queen(Color.WHITE)
    assert Square(Column.E, 7) not in piece_dict
    assert not capture

    move = QueenPromotion(Square(Column.E, 2), Square(Column.E, 1))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.E, 1)] == Queen(Color.BLACK)
    assert Square(Column.E, 2) not in piece_dict
    assert not capture


def test_apply_knight_promotion_capture():
    """
    Test a knight promotion
    8 | | | | | |b| | |
    7 | | | | |W| | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | |B| | | |
    1 | | | | | |w | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.E, 7): Pawn(Color.WHITE),
        Square(Column.E, 2): Pawn(Color.BLACK),
        Square(Column.F, 8): Piece(Color.BLACK),
        Square(Column.F, 1): Piece(Color.WHITE),
    }
    move = KnightPromotionCapture(Square(Column.E, 7), Square(Column.F, 8))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.F, 8)] == Knight(Color.WHITE)
    assert Square(Column.E, 7) not in piece_dict
    assert capture

    move = KnightPromotionCapture(Square(Column.E, 2), Square(Column.F, 1))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.F, 1)] == Knight(Color.BLACK)
    assert Square(Column.E, 2) not in piece_dict
    assert capture


def test_apply_queen_promotion_capture():
    """
    Test a knight promotion
    8 | | | | | |b| | |
    7 | | | | |W| | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | |B| | | |
    1 | | | | | |w| | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.E, 7): Pawn(Color.WHITE),
        Square(Column.E, 2): Pawn(Color.BLACK),
        Square(Column.F, 8): Piece(Color.BLACK),
        Square(Column.F, 1): Piece(Color.WHITE),
    }
    move = QueenPromotionCapture(Square(Column.E, 7), Square(Column.F, 8))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.F, 8)] == Queen(Color.WHITE)
    assert Square(Column.E, 7) not in piece_dict
    assert capture

    move = QueenPromotionCapture(Square(Column.E, 2), Square(Column.F, 1))
    capture = move.apply_move(piece_dict)
    assert piece_dict[Square(Column.F, 1)] == Queen(Color.BLACK)
    assert Square(Column.E, 2) not in piece_dict
    assert capture
