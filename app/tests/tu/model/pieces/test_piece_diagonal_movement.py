"""
Tests for piece (diagonal movements)
"""
from itertools import product

from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.pieces.piece import Piece
from app.src.model.pieces.rook import Rook


class TestPiece:
    """
    Test class
    """

    square_list = {
        (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
    }

    def test_available_squares_diagonal_right_up_case1(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |W| | |
        5 | | | | | | | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.F, 6)

        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 6): other1,
        }
        expected_squares = [
            self.square_list[Column.E, 5],
        ]
        assert (
            piece._available_squares_diagonal_right_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_right_up_case2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |B| | |
        5 | | | | | | | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.F, 6, Color.BLACK)
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 6): other1,
        }
        expected_squares = [
            self.square_list[Column.E, 5],
            self.square_list[Column.F, 6],
        ]
        assert (
            piece._available_squares_diagonal_right_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_right_up_case3(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | |W| | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 5)
        piece_list = {
            (Column.D, 5): piece,
        }
        expected_squares = [
            self.square_list[Column.E, 6],
            self.square_list[Column.F, 7],
            self.square_list[Column.G, 8],
        ]
        assert (
            piece._available_squares_diagonal_right_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_right_up_case4(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | |W|
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.H, 7)
        piece_list = {
            (Column.H, 7): piece,
        }
        expected_squares = []
        assert (
            piece._available_squares_diagonal_right_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_right_up_case5(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | |W| | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.E, 5)
        piece_list = {
            (Column.D, 4): piece,
            (Column.E, 5): other1,
        }
        expected_squares = []
        assert (
            piece._available_squares_diagonal_right_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_right_down_case1(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | | | | | |W| | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.F, 2)
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 2): other1,
        }
        expected_squares = [
            self.square_list[Column.E, 3],
        ]
        assert (
            piece._available_squares_diagonal_right_down(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_right_down_case2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | | | | | |B| | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.F, 2, Color.BLACK)
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 2): other1,
        }
        expected_squares = [
            self.square_list[Column.E, 3],
            self.square_list[Column.F, 2],
        ]
        assert (
            piece._available_squares_diagonal_right_down(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_right_down_case3(self):
        """
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
        piece = Rook(Column.D, 4)
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = [
            self.square_list[Column.E, 3],
            self.square_list[Column.F, 2],
            self.square_list[Column.G, 1],
        ]
        assert (
            piece._available_squares_diagonal_right_down(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_right_down_case4(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | |W| | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.F, 1)
        piece_list = {
            (Column.F, 1): piece,
        }
        expected_squares = []
        assert (
            piece._available_squares_diagonal_right_down(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_right_down_case5(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | |W| | | | |
        2 | | | | |W| | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 3)
        other = Piece(Column.E, 2)
        piece_list = {
            (Column.F, 1): piece,
            (Column.E, 2): other,
        }
        expected_squares = []
        assert (
            piece._available_squares_diagonal_right_down(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_up_case1(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | |W| | | | | | |
        5 | | | | | | | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.B, 6)
        piece_list = {
            (Column.D, 4): piece,
            (Column.B, 6): other1,
        }
        expected_squares = [
            self.square_list[Column.C, 5],
        ]
        assert (
            piece._available_squares_diagonal_left_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_up_case2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | |B| | | | | | |
        5 | | | | | | | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.B, 6, Color.BLACK)
        piece_list = {
            (Column.D, 4): piece,
            (Column.B, 6): other1,
        }
        expected_squares = [
            self.square_list[Column.C, 5],
            self.square_list[Column.B, 6],
        ]
        assert (
            piece._available_squares_diagonal_left_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_up_case3(self):
        """
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
        piece = Rook(Column.D, 4)
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = [
            self.square_list[Column.C, 5],
            self.square_list[Column.B, 6],
            self.square_list[Column.A, 7],
        ]
        assert (
            piece._available_squares_diagonal_left_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_up_case4(self):
        """
        8 | | | | | | | | |
        7 |W| | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.A, 7)
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = []
        assert (
            piece._available_squares_diagonal_left_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_up_case5(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | |W| | | | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other = Piece(Column.C, 5)
        piece_list = {
            (Column.D, 4): piece,
            (Column.C, 5): other,
        }
        expected_squares = []
        assert (
            piece._available_squares_diagonal_left_up(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_down_case1(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | |W| | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.B, 2)
        piece_list = {
            (Column.D, 4): piece,
            (Column.B, 2): other1,
        }
        expected_squares = [
            self.square_list[Column.C, 3],
        ]
        assert (
            piece._available_squares_diagonal_left_down(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_down_case2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |W| | | | |
        3 | | | | | | | | |
        2 | |B| | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.B, 2, Color.BLACK)
        piece_list = {
            (Column.D, 4): piece,
            (Column.B, 2): other1,
        }
        expected_squares = [
            self.square_list[Column.C, 3],
            self.square_list[Column.B, 2],
        ]
        assert (
            piece._available_squares_diagonal_left_down(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_down_case3(self):
        """
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
        piece = Rook(Column.D, 4)
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = [
            self.square_list[Column.C, 3],
            self.square_list[Column.B, 2],
            self.square_list[Column.A, 1],
        ]
        assert (
            piece._available_squares_diagonal_left_down(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_down_case4(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 |W| | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.A, 2)
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = []
        assert (
            piece._available_squares_diagonal_left_down(self.square_list, piece_list)
            == expected_squares
        )

    def test_available_squares_diagonal_left_down_case5(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |W| | | | |
        3 | | |W| | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.C, 3)
        piece_list = {
            (Column.D, 4): piece,
            (Column.C, 3): other1,
        }
        expected_squares = []
        assert (
            piece._available_squares_diagonal_left_down(self.square_list, piece_list)
            == expected_squares
        )
