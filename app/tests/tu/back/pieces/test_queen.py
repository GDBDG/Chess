"""
Tests for the queen
"""
from itertools import product

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.back.pieces.piece import Piece
from app.src.back.pieces.queen import Queen


def test_queen():
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
    (The rook moves uses _available_square_on_side_line, already completely
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
