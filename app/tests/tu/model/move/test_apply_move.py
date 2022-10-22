"""
Tests moves application
"""
from app.src.model.events.moves.en_passant import EnPassant
from app.src.model.events.moves.knight_promotion import KnightPromotion
from app.src.model.events.moves.knight_promotion_capture import KnightPromotionCapture
from app.src.model.events.moves.long_castling import LongCastling
from app.src.model.events.moves.move import Move
from app.src.model.events.moves.queen_promotion import QueenPromotion
from app.src.model.events.moves.queen_promotion_capture import QueenPromotionCapture
from app.src.model.events.moves.short_castling import ShortCastling
from app.src.model.game.board import Board
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.pieces.king import King
from app.src.model.pieces.knight import Knight
from app.src.model.pieces.pawn import Pawn
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.queen import Queen
from app.src.model.pieces.rook import Rook


def test_apply_move_no_capture():
    """
    Test that a moves is applied
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
    board = Board()
    board.piece_dict = piece_dict
    move = Move(Square(Column.E, 2), Square(Column.E, 4))
    capture = move.apply_move(board)
    assert piece_dict[Square(Column.E, 4)] == Piece(Color.WHITE)
    assert Square(Column.E, 2) not in piece_dict
    assert not capture


def test_apply_move_capture():
    """
    Test that a moves is applied
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
    board = Board()
    piece_dict = {
        Square(Column.E, 2): Piece(Color.WHITE),
        Square(Column.E, 4): Piece(Color.BLACK),
    }
    board.piece_dict = piece_dict
    move = Move(Square(Column.E, 2), Square(Column.E, 4))
    capture = move.apply_move(board)
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


def test_apply_en_passant():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | |p|P|p| | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    Test that EnPassant Move is correctly applied
    @return:
    """
    piece_dict = {
        Square(Column.E, 5): Pawn(Color.WHITE),
        Square(Column.F, 5): Pawn(Color.BLACK),
        Square(Column.D, 5): Pawn(Color.BLACK),
    }
    move = EnPassant(
        Square(Column.E, 5),
        Square(Column.F, 6),
    )
    capture = move.apply_move(piece_dict)
    assert capture
    assert piece_dict[Square(Column.D, 5)] == Pawn(Color.BLACK)
    assert piece_dict[Square(Column.F, 6)] == Pawn(Color.WHITE)
    assert Square(Column.E, 5) not in piece_dict
    assert Square(Column.F, 5) not in piece_dict


def test_apply_long_castling():
    """
    Test that a valid long castling is applied correctly
    1 |R| | | |K| | | |
       A B C D E F G H
    1 | | |K|R| | | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
    }
    LongCastling(Square(Column.E, 1)).apply_move(piece_dict)
    assert Square(Column.A, 1) not in piece_dict
    assert Square(Column.E, 1) not in piece_dict
    assert piece_dict[Square(Column.C, 1)] == King(Color.WHITE)
    assert piece_dict[Square(Column.D, 1)] == Rook(Color.WHITE)


def test_apply_short_castling():
    """
    Test that a valid long castling is applied correctly
    1 | | | | |K| | |R|
       A B C D E F G H
    1 | | | | | |R|K| |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
    }
    ShortCastling(Square(Column.E, 1)).apply_move(piece_dict)
    assert Square(Column.H, 1) not in piece_dict
    assert Square(Column.E, 1) not in piece_dict
    assert piece_dict[Square(Column.G, 1)] == King(Color.WHITE)
    assert piece_dict[Square(Column.F, 1)] == Rook(Color.WHITE)
