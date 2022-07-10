"""
test knight
"""
from itertools import product

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.back.pieces.knight import Knight
from app.src.back.pieces.piece import Piece


class TestKnight:
    """
    Class test
    """

    square_list = {
        (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
    }

    def test_knight1(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |x| |x| | | |
        5 | |x| | | |x| | |
        4 | | | |W| | | | |
        3 | |x| | | |x| | |
        2 | | |x| |x| | | |
        1 | | | | | | | | |
           A B C D E F G H
        :return: None
        """
        piece = Knight(Column.D, 4)
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = [
            self.square_list[Column.C, 6],
            self.square_list[Column.E, 6],
            self.square_list[Column.C, 2],
            self.square_list[Column.E, 2],
            self.square_list[Column.F, 3],
            self.square_list[Column.F, 5],
            self.square_list[Column.B, 3],
            self.square_list[Column.B, 5],
        ]
        assert piece.available_squares(self.square_list, piece_list) == expected_squares

    def test_knight2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 |x| |x| | | | | |
        3 | | | |x| | | | |
        2 | |W| | | | | | |
        1 | | | |x| | | | |
           A B C D E F G H
        :return: None
        """
        piece = Knight(Column.B, 2)
        piece_list = {
            (Column.B, 2): piece,
        }
        expected_squares = [
            self.square_list[Column.A, 4],
            self.square_list[Column.C, 4],
            self.square_list[Column.D, 1],
            self.square_list[Column.D, 3],
        ]
        assert piece.available_squares(self.square_list, piece_list) == expected_squares

    def test_knight3(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |x| |W| | | |
        5 | |W| | | |B| | |
        4 | | | |W| | | | |
        3 | |x| | | |x| | |
        2 | | |x| |B| | | |
        1 | | | | | | | | |
           A B C D E F G H
        :return: None
        """
        piece = Knight(Column.D, 4)
        other1 = Piece(Column.E, 6)
        other2 = Piece(Column.F, 5, Color.BLACK)
        other3 = Piece(Column.E, 2, Color.BLACK)
        other4 = Piece(Column.B, 5)
        piece_list = {
            (Column.D, 4): piece,
            (Column.E, 6): other1,
            (Column.F, 5): other2,
            (Column.E, 2): other3,
            (Column.B, 5): other4,
        }
        expected_squares = [
            self.square_list[Column.C, 6],
            self.square_list[Column.C, 2],
            self.square_list[Column.E, 2],
            self.square_list[Column.F, 3],
            self.square_list[Column.F, 5],
            self.square_list[Column.B, 3],
        ]
        assert piece.available_squares(self.square_list, piece_list) == expected_squares
