"""
Tests for Move classes
"""
from src.CHESS.domain.classes.const.color import Color
from src.CHESS.domain.classes.const.column import Column
from src.CHESS.domain.classes.pieces.king import King
from src.CHESS.domain.classes.pieces.piece import Piece
from src.CHESS.domain.classes.pieces.rook import Rook
from src.CHESS.domain.classes.square import Square
from src.CHESS.domain.events.event_processor.move_processor import (
    is_move_legal,
    square_available_moves_no_castling,
)
from src.CHESS.domain.events.moves.move import Move
from src.CHESS.domain.events.moves.rook_move import RookMove
from src.CHESS.domain.states.board import Board


def test_is_legal():
    """
    Test that a legal moves is detected as legal
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
    board = Board()
    board.piece_dict = piece_dict
    move = Move(Square(Column.D, 4), Square(Column.C, 3))
    assert is_move_legal(move, board)


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
    board = Board()
    board.piece_dict = piece_dict
    move = Move(Square(Column.A, 1), Square(Column.B, 1))
    assert not is_move_legal(move, board)


def test_is_not_legal2():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 |K| |O| |r| | | |
       A B C D E F G H
    @return:
    """
    piece_dict = {
        Square(Column.A, 1): King(Color.WHITE),
        Square(Column.E, 1): Rook(Color.BLACK),
        Square(Column.C, 1): Piece(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    move = Move(Square(Column.C, 1), Square(Column.C, 2))
    assert not is_move_legal(move, board)


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
    board = Board()
    board.piece_dict = piece_dict
    expected_moves = [
        RookMove(Square(Column.C, 1), Square(Column.D, 1)),
        RookMove(Square(Column.C, 1), Square(Column.E, 1)),
        RookMove(Square(Column.C, 1), Square(Column.B, 1)),
    ]
    assert (
        square_available_moves_no_castling(
            Square(Column.C, 1), board, legal_verification=True
        )
        == expected_moves
    )
