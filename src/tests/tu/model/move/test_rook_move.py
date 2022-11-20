"""
Unit tests for the rook moves
"""
from src.domain.classes.const.color import Color
from src.domain.classes.const.column import Column
from src.domain.classes.pieces.piece import Piece
from src.domain.classes.pieces.rook import Rook
from src.domain.classes.square import Square
from src.domain.events.event_processor.move_processor import (
    square_available_moves_no_castling,
)
from src.domain.events.moves.rook_move import RookMove
from src.domain.states.board import Board


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
    board = Board()
    board.piece_dict = piece_dict
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
        square_available_moves_no_castling(Square(Column.D, 4), board) == expected_moves
    )
