"""
Test for the king
"""
from itertools import product

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.back.pieces.king import King
from app.src.back.pieces.piece import Piece
from app.src.back.pieces.rook import Rook


class TestKing:
    """
    Test class
    """

    square_list = {
        (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
    }

    def test_available_squares(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |W|W| | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        No need to do extensive tests, since they are done in the Piece tests
        (The rook moves uses _available_square_on_side_line, already completely
        tested)
        :return:
        """
        piece = King(Column.D, 4)
        other = Piece(Column.E, 4)

        piece_list = {
            (Column.D, 4): piece,
            (Column.E, 4): other,
        }
        expected_squares = [
            self.square_list[Column.C, 3],
            self.square_list[Column.C, 4],
            self.square_list[Column.C, 5],
            self.square_list[Column.D, 3],
            self.square_list[Column.D, 5],
            self.square_list[Column.E, 3],
            self.square_list[Column.E, 5],
        ]
        assert piece.available_squares(self.square_list, piece_list) == expected_squares

    def test_available_squares2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |W|B| | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        No need to do extensive tests, since they are done in the Piece tests
        (The rook moves uses _available_square_on_side_line, already completely
        tested)
        :return:
        """
        piece = King(Column.D, 4)
        other = Piece(Column.E, 4, Color.BLACK)

        piece_list = {
            (Column.D, 4): piece,
            (Column.E, 4): other,
        }
        expected_squares = [
            self.square_list[Column.E, 4],
        ]
        assert piece.available_squares(self.square_list, piece_list) == expected_squares

    def test_available_squares3(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 |W| | | |B| | | |
           A B C D E F G H
        No need to do extensive tests, since they are done in the Piece tests
        (The rook moves uses _available_square_on_side_line, already completely
        tested)
        :return:
        """
        piece = King(Column.A, 1)
        other = Rook(Column.E, 1, Color.BLACK)

        piece_list = {
            (Column.A, 1): piece,
            (Column.E, 1): other,
        }
        expected_squares = [
            self.square_list[Column.A, 2],
            self.square_list[Column.B, 2],
        ]
        assert piece.available_squares(self.square_list, piece_list) == expected_squares
