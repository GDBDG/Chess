"""
Tests for the pawn moves
"""
from app.src.model.game.game import Game
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.en_passant import EnPassant
from app.src.model.move.knight_promotion import KnightPromotion
from app.src.model.move.knight_promotion_capture import KnightPromotionCapture
from app.src.model.move.pawn_2_square_move import Pawn2SquareMove
from app.src.model.move.pawn_capture import CaptureMove
from app.src.model.move.pawn_move import PawnMove
from app.src.model.move.queen_promotion import QueenPromotion
from app.src.model.move.queen_promotion_capture import QueenPromotionCapture
from app.src.model.pieces.pawn import Pawn
from app.src.model.pieces.piece import Piece


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
    game = Game()
    game.piece_dict = piece_dict
    expected_white_move = [PawnMove(Square(Column.E, 3), Square(Column.E, 4))]
    expected_black_move = [PawnMove(Square(Column.C, 6), Square(Column.C, 5))]
    assert (
        game.square_available_moves_no_castling(Square(Column.E, 3))
        == expected_white_move
    )
    assert (
        game.square_available_moves_no_castling(Square(Column.C, 6))
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
    game = Game()
    game.piece_dict = piece_dict
    expected_white_move = [
        QueenPromotion(Square(Column.E, 7), Square(Column.E, 8)),
        KnightPromotion(Square(Column.E, 7), Square(Column.E, 8)),
    ]
    expected_black_move = [
        QueenPromotion(Square(Column.C, 2), Square(Column.C, 1)),
        KnightPromotion(Square(Column.C, 2), Square(Column.C, 1)),
    ]
    assert (
        game.square_available_moves_no_castling(Square(Column.E, 7))
        == expected_white_move
    )
    assert (
        game.square_available_moves_no_castling(Square(Column.C, 2))
        == expected_black_move
    )


def test_available_capture():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | |B| | | | | |
    5 | |w|b|w| | | | |
    4 | | | |b|w|b| | |
    3 | | | | |W| | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    Test that a pawn can capture a piece
    @return:
    """
    piece_dict = {
        Square(Column.E, 3): Pawn(Color.WHITE),
        Square(Column.C, 6): Pawn(Color.BLACK),
        Square(Column.D, 4): Piece(Color.BLACK),
        Square(Column.E, 4): Piece(Color.WHITE),
        Square(Column.F, 4): Piece(Color.BLACK),
        Square(Column.B, 5): Piece(Color.WHITE),
        Square(Column.C, 5): Piece(Color.BLACK),
        Square(Column.D, 5): Piece(Color.WHITE),
    }
    game = Game()
    game.piece_dict = piece_dict
    expected_white = [
        CaptureMove(Square(Column.E, 3), Square(Column.F, 4)),
        CaptureMove(Square(Column.E, 3), Square(Column.D, 4)),
    ]
    expected_black = [
        CaptureMove(Square(Column.C, 6), Square(Column.D, 5)),
        CaptureMove(Square(Column.C, 6), Square(Column.B, 5)),
    ]
    assert (
        game.square_available_moves_no_castling(Square(Column.E, 3)) == expected_white
    )
    assert (
        game.square_available_moves_no_castling(Square(Column.C, 6)) == expected_black
    )


def test_available_promotion():
    """
    8 | | | | |B| | | |
    7 | | | | | |W| | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    Test that a promotion return 2 Moves
    @return:
    """
    piece_dict = {
        Square(Column.F, 7): Pawn(Color.WHITE),
        Square(Column.E, 8): Piece(Color.BLACK),
    }
    game = Game()
    game.piece_dict = piece_dict
    expected_moves = [
        QueenPromotion(Square(Column.F, 7), Square(Column.F, 8)),
        KnightPromotion(Square(Column.F, 7), Square(Column.F, 8)),
        QueenPromotionCapture(Square(Column.F, 7), Square(Column.E, 8)),
        KnightPromotionCapture(Square(Column.F, 7), Square(Column.E, 8)),
    ]
    assert (
        game.square_available_moves_no_castling(Square(Column.F, 7)) == expected_moves
    )


def test_initial_move():
    """
    8 | | | | | | | | |
    7 | | |B| | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | |W| | | |
    1 | | | | | | | | |
       A B C D E F G H
    Test that a pawn can move of 2 squares for its first movement
    @return:
    """
    piece_dict = {
        Square(Column.E, 2): Pawn(Color.WHITE),
        Square(Column.C, 7): Pawn(Color.BLACK),
    }
    game = Game()
    game.piece_dict = piece_dict
    expected_white = [
        Pawn2SquareMove(Square(Column.E, 2), Square(Column.E, 4)),
        PawnMove(Square(Column.E, 2), Square(Column.E, 3)),
    ]
    expected_black = [
        Pawn2SquareMove(Square(Column.C, 7), Square(Column.C, 5)),
        PawnMove(Square(Column.C, 7), Square(Column.C, 6)),
    ]
    assert (
        game.square_available_moves_no_castling(Square(Column.E, 2)) == expected_white
    )
    assert (
        game.square_available_moves_no_castling(Square(Column.C, 7)) == expected_black
    )


def test_en_passant_available_destination():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | |x| | |
    5 | | | | | |B|W|B|
    4 |W|B|W| | | | | |
    3 | | |x| | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    Test that the correct destination is returned if en passant available
    @return:
    """
    piece_dict = {
        Square(Column.A, 4): Pawn(Color.WHITE),
        Square(Column.B, 4): Pawn(Color.BLACK),
        Square(Column.C, 4): Pawn(Color.WHITE),
        Square(Column.F, 5): Pawn(Color.BLACK),
        Square(Column.G, 5): Pawn(Color.WHITE),
        Square(Column.H, 5): Pawn(Color.BLACK),
    }
    game = Game()
    game.piece_dict = piece_dict

    last_move_white = Pawn2SquareMove(
        Square(Column.C, 2),
        Square(Column.C, 4),
    )
    game.move_historic.append(last_move_white)
    expected_moves = [
        PawnMove(Square(Column.B, 4), Square(Column.B, 3)),
        EnPassant(Square(Column.B, 4), Square(Column.C, 3)),
    ]
    assert (
        game.square_available_moves_no_castling(Square(Column.B, 4)) == expected_moves
    )

    last_move_black = Pawn2SquareMove(
        Square(Column.F, 7),
        Square(Column.F, 5),
    )
    game.move_historic.append(last_move_black)
    expected_moves = [
        PawnMove(Square(Column.G, 5), Square(Column.G, 6)),
        EnPassant(Square(Column.G, 5), Square(Column.F, 6)),
    ]
    assert (
        game.square_available_moves_no_castling(Square(Column.G, 5)) == expected_moves
    )


def test_en_passant_available_destination_none():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | |x| | |
    5 | | | | | |B|W|B|
    4 |W|B|W| | | | | |
    3 | | |x| | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    Test that if the last move does not allow en passant, None is returned
    @return:
    """
    piece_dict = {
        Square(Column.A, 4): Pawn(Color.WHITE),
        Square(Column.B, 4): Pawn(Color.BLACK),
        Square(Column.C, 4): Pawn(Color.WHITE),
        Square(Column.F, 5): Pawn(Color.BLACK),
        Square(Column.G, 5): Pawn(Color.WHITE),
        Square(Column.H, 5): Pawn(Color.BLACK),
    }
    game = Game()
    game.piece_dict = piece_dict

    last_move_white = PawnMove(
        Square(Column.C, 3),
        Square(Column.C, 4),
    )
    game.move_historic.append(last_move_white)
    expected_moves = [
        PawnMove(Square(Column.B, 4), Square(Column.B, 3)),
    ]
    assert (
        game.square_available_moves_no_castling(Square(Column.B, 4)) == expected_moves
    )

    last_move_black = PawnMove(
        Square(Column.F, 6),
        Square(Column.F, 5),
    )
    expected_moves = [
        PawnMove(Square(Column.G, 5), Square(Column.G, 6)),
    ]
    game.move_historic.append(last_move_black)
    assert (
        game.square_available_moves_no_castling(Square(Column.G, 5)) == expected_moves
    )
