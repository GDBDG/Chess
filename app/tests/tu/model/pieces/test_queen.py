"""
Tests for the queen
"""
from itertools import product

from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.move import Move, EmptyMove
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.queen import Queen


def test_available_squares():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | |W| |B| | |
    5 | | | | | | | | |
    4 | | | |W| | |B| |
    3 | | |W| | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    No need to do extensive tests, since they are done in the Piece tests
    (The queen moves uses _available_square_on_side_line, already completely
    tested)
    :return:
    """
    piece = Queen(Column.D, 4)
    other1 = Piece(Column.D, 6)
    other2 = Piece(Column.G, 4, Color.BLACK)
    other3 = Piece(Column.F, 6, Color.BLACK)
    other4 = Piece(Column.C, 3)
    square_list = {
        (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
    }
    piece_list = {
        (Column.D, 4): piece,
        (Column.D, 6): other1,
        (Column.G, 4): other2,
        (Column.F, 6): other3,
        (Column.C, 3): other4,
    }
    expected_squares = [
        square_list[Column.E, 4],
        square_list[Column.F, 4],
        square_list[Column.G, 4],
        square_list[Column.C, 4],
        square_list[Column.B, 4],
        square_list[Column.A, 4],
        square_list[Column.D, 5],
        square_list[Column.D, 3],
        square_list[Column.D, 2],
        square_list[Column.D, 1],
        square_list[Column.E, 5],
        square_list[Column.F, 6],
        square_list[Column.E, 3],
        square_list[Column.F, 2],
        square_list[Column.G, 1],
        square_list[Column.C, 5],
        square_list[Column.B, 6],
        square_list[Column.A, 7],
    ]
    assert piece.available_squares(square_list, piece_list) == expected_squares


def test_available_moves():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | |W| | | | | |
    2 |W| | | | | | | |
    1 |W| |W| | | | | |
       A B C D E F G H
    :return:
    """
    piece = Queen(Column.A, 1)
    other1 = Piece(Column.A, 2)
    other2 = Piece(Column.C, 1)
    other3 = Piece(Column.C, 3)
    square_list = {
        (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
    }
    piece_list = {
        (Column.A, 1): piece,
        (Column.A, 2): other1,
        (Column.C, 1): other2,
        (Column.C, 3): other3,
    }
    expected_moves = [
        Move(square_list[Column.A, 1], square_list[Column.B, 1], PieceType.QUEEN),
        Move(square_list[Column.A, 1], square_list[Column.B, 2], PieceType.QUEEN),
    ]
    assert (
        piece._available_moves_no_legal_verification(
            square_list, piece_list, EmptyMove()
        )
        == expected_moves
    )
