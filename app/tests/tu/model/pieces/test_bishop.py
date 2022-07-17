"""
Tests for the bishop
"""
from itertools import product

from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.move import Move
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.pieces.bishop import Bishop
from app.src.model.pieces.piece import Piece


def test_move_to():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | |W| | |
    5 | | | | | | | | |
    4 | | | |W| | | | |
    3 | | | | | | | | |
    2 | |B| | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    No need to do extensive tests, since they are done in the Piece tests
    (The bishop moves uses _available_square_on_side_line, already completely
    tested)
    :return:
    """
    piece = Bishop(Column.D, 4)
    other1 = Piece(Column.F, 6)
    other2 = Piece(Column.B, 2, Color.BLACK)
    square_list = {
        (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
    }
    piece_list = {
        (Column.D, 4): piece,
        (Column.F, 6): other1,
        (Column.B, 2): other2,
    }
    expected_squares = [
        square_list[Column.E, 5],
        square_list[Column.E, 3],
        square_list[Column.F, 2],
        square_list[Column.G, 1],
        square_list[Column.C, 5],
        square_list[Column.B, 6],
        square_list[Column.A, 7],
        square_list[Column.C, 3],
        square_list[Column.B, 2],
    ]
    assert piece.available_squares(square_list, piece_list) == expected_squares


def test_available_moves():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | |B| | | | | | |
    1 |W| | | | | | | |
       A B C D E F G H
    No need to do extensive tests, this feature uses the available_squares feature,
    already tested
    :return:
    """
    piece = Bishop(Column.A, 1)
    other1 = Piece(Column.B, 2, Color.BLACK)
    square_list = {
        (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
    }
    piece_list = {
        (Column.A, 1): piece,
        (Column.B, 2): other1,
    }
    expected_moves = [
        Move(square_list[Column.A, 1], square_list[Column.B, 2], PieceType.BISHOP)
    ]
    available_moves = piece.available_moves(square_list, piece_list)
    assert available_moves == expected_moves
