"""
Tests for the rook
"""
from itertools import product

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.back.pieces.piece import Piece
from app.src.back.pieces.rook import Rook


def test_rook():
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
    No need to do extensive tests, since they are done in the Piece tests
    (The rook moves uses _available_square_on_side_line, already completely
    tested)
    :return:
    """
    piece = Rook(Column.D, 4)
    other1 = Piece(Column.D, 6)
    other2 = Piece(Column.G, 4, Color.BLACK)
    square_list = {(col, row): Square(col, row) for col, row in product(Column, range(1, 9))}
    piece_list = {
        (Column.D, 4): piece,
        (Column.D, 6): other1,
        (Column.G, 4): other2,
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

    ]
    assert (
            piece.available_squares(square_list, piece_list) == expected_squares
    )
