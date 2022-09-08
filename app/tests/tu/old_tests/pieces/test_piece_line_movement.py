"""
Tests for piece class
(Tests for movement checks in line
"""
from app.src.old_model.chess_board.square import Square
from app.src.old_model.miscenaleous.color import Color
from app.src.old_model.miscenaleous.column import Column
from app.src.old_model.pieces.piece import Piece


class TestPiece:
    """
    test class
    """

    def test_available_square_on_right_case1(self):
        """
        1 | | |W| | |W| | |
           A B C D E F G H
        @return:
        """
        piece = Piece(Column.C, 1)
        other = Piece(Column.F, 1)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {(Column.C, 1): piece, (Column.F, 1): other}
        expected_squares = [
            square_list[Column.D, 1],
            square_list[Column.E, 1],
        ]
        assert (
            piece._available_squares_on_right(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_on_right_case2(self):
        """
        1 | | |W| | |B| | |
           A B C D E F G H
        @return:
        """
        piece = Piece(Column.C, 1)
        other = Piece(Column.F, 1, Color.BLACK)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {(Column.C, 1): piece, (Column.F, 1): other}
        expected_squares = [
            square_list[Column.D, 1],
            square_list[Column.E, 1],
            square_list[Column.F, 1],
        ]
        assert (
            piece._available_squares_on_right(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_on_right_case3(self):
        """
        1 | | |W| | | | | |
           A B C D E F G H
        @return:
        """
        piece = Piece(Column.C, 1)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {
            (Column.C, 1): piece,
        }
        expected_squares = [
            square_list[Column.D, 1],
            square_list[Column.E, 1],
            square_list[Column.F, 1],
            square_list[Column.G, 1],
            square_list[Column.H, 1],
        ]
        assert (
            piece._available_squares_on_right(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_on_right_case4(self):
        """
         1 | | | | | | | |W|
            A B C D E F G H
        @return:
        """
        piece = Piece(Column.H, 1)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {
            (Column.H, 1): piece,
        }
        expected_squares = []
        assert (
            piece._available_squares_on_right(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_on_right_case5(self):
        """
        1 | | |W|W| | | | |
           A B C D E F G H
        @return:
        """
        piece = Piece(Column.C, 1)
        other = Piece(Column.D, 1)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {(Column.C, 1): piece, (Column.D, 1): other}
        expected_squares = []
        assert (
            piece._available_squares_on_right(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_on_left_case1(self):
        """
        1 | | |W| | |W| | |
           A B C D E F G H
        @return:
        """
        other = Piece(Column.C, 1)
        piece = Piece(Column.F, 1)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {(Column.F, 1): piece, (Column.C, 1): other}
        expected_squares = [
            square_list[Column.E, 1],
            square_list[Column.D, 1],
        ]
        assert (
            piece._available_squares_on_left(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_on_left_case2(self):
        """
        1 | | |W| | |B| | |
           A B C D E F G H
        @return:
        """
        other = Piece(Column.C, 1)
        piece = Piece(Column.F, 1, Color.BLACK)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {(Column.F, 1): piece, (Column.C, 1): other}
        expected_squares = [
            square_list[Column.E, 1],
            square_list[Column.D, 1],
            square_list[Column.C, 1],
        ]
        assert (
            piece._available_squares_on_left(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_on_left_case3(self):
        """
        1 | | |W| | | | | |
           A B C D E F G H
        @return:
        """
        piece = Piece(Column.C, 1)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {
            (Column.C, 1): piece,
        }
        expected_squares = [
            square_list[Column.B, 1],
            square_list[Column.A, 1],
        ]
        assert (
            piece._available_squares_on_left(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_on_left_case4(self):
        """
         1 |W| | | | | | | |
            A B C D E F G H
        @return:
        """
        piece = Piece(Column.A, 1)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {
            (Column.A, 1): piece,
        }
        expected_squares = []
        assert (
            piece._available_squares_on_left(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_on_left_case5(self):
        """
        1 | | |W|W| | | | |
           A B C D E F G H
        @return:
        """
        other = Piece(Column.C, 1)
        piece = Piece(Column.D, 1)
        square_list = {(col, 1): Square(col, 1) for col in Column}
        piece_list = {(Column.D, 1): piece, (Column.C, 1): other}
        expected_squares = []
        assert (
            piece._available_squares_on_left(square_list, piece_list)
            == expected_squares
        )

    def test_available_square_upper_case1(self):
        """
        8 | |
        7 | |
        6 |W|
        5 | |
        4 | |
        3 | |
        2 |W|
        1 | |
           A
        @return:
        """
        piece = Piece(Column.A, 2)
        other = Piece(Column.A, 6)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {(Column.A, 2): piece, (Column.A, 6): other}
        expected_squares = [
            square_list[Column.A, 3],
            square_list[Column.A, 4],
            square_list[Column.A, 5],
        ]
        assert (
            piece._available_squares_upper(square_list, piece_list) == expected_squares
        )

    def test_available_square_upper_case2(self):
        """
        8 | |
        7 | |
        6 |B|
        5 | |
        4 | |
        3 | |
        2 |W|
        1 | |
           A
        @return:
        """
        piece = Piece(Column.A, 2)
        other = Piece(Column.A, 6, Color.BLACK)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {(Column.A, 2): piece, (Column.A, 6): other}
        expected_squares = [
            square_list[Column.A, 3],
            square_list[Column.A, 4],
            square_list[Column.A, 5],
            square_list[Column.A, 6],
        ]
        assert (
            piece._available_squares_upper(square_list, piece_list) == expected_squares
        )

    def test_available_square_upper_case3(self):
        """
        8 | |
        7 | |
        6 | |
        5 | |
        4 | |
        3 | |
        2 |W|
        1 | |
           A
        @return:
        """
        piece = Piece(Column.A, 2)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {
            (Column.A, 2): piece,
        }
        expected_squares = [
            square_list[Column.A, 3],
            square_list[Column.A, 4],
            square_list[Column.A, 5],
            square_list[Column.A, 6],
            square_list[Column.A, 7],
            square_list[Column.A, 8],
        ]
        assert (
            piece._available_squares_upper(square_list, piece_list) == expected_squares
        )

    def test_available_square_upper_case4(self):
        """
        8 |W|
        7 | |
        6 | |
        5 | |
        4 | |
        3 | |
        2 | |
        1 | |
           A
        @return:
        """
        piece = Piece(Column.A, 8)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {
            (Column.A, 8): piece,
        }
        expected_squares = []
        assert (
            piece._available_squares_upper(square_list, piece_list) == expected_squares
        )

    def test_available_square_upper_case5(self):
        """
        8 | |
        7 | |
        6 | |
        5 | |
        4 | |
        3 |W|
        2 |W|
        1 | |
           A
        @return:
        """
        piece = Piece(Column.A, 2)
        other = Piece(Column.A, 3)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {(Column.A, 2): piece, (Column.A, 3): other}
        expected_squares = []
        assert (
            piece._available_squares_upper(square_list, piece_list) == expected_squares
        )

    def test_available_square_below_case1(self):
        """
        8 | |
        7 | |
        6 |W|
        5 | |
        4 | |
        3 | |
        2 |W|
        1 | |
           A
        @return:
        """
        piece = Piece(Column.A, 6)
        other = Piece(Column.A, 2)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {(Column.A, 6): piece, (Column.A, 2): other}
        expected_squares = [
            square_list[Column.A, 5],
            square_list[Column.A, 4],
            square_list[Column.A, 3],
        ]
        assert (
            piece._available_squares_below(square_list, piece_list) == expected_squares
        )

    def test_available_square_below_case2(self):
        """
        8 | |
        7 | |
        6 |B|
        5 | |
        4 | |
        3 | |
        2 |W|
        1 | |
           A
        @return:
        """
        piece = Piece(Column.A, 6, Color.BLACK)
        other = Piece(Column.A, 2)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {(Column.A, 6): piece, (Column.A, 2): other}
        expected_squares = [
            square_list[Column.A, 5],
            square_list[Column.A, 4],
            square_list[Column.A, 3],
            square_list[Column.A, 2],
        ]
        assert (
            piece._available_squares_below(square_list, piece_list) == expected_squares
        )

    def test_available_square_below_case3(self):
        """
        8 | |
        7 | |
        6 | |
        5 | |
        4 | |
        3 | |
        2 |W|
        1 | |
           A
        @return:
        """
        piece = Piece(Column.A, 2)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {
            (Column.A, 2): piece,
        }
        expected_squares = [
            square_list[Column.A, 1],
        ]
        assert (
            piece._available_squares_below(square_list, piece_list) == expected_squares
        )

    def test_available_square_below_case4(self):
        """
        8 | |
        7 | |
        6 | |
        5 | |
        4 | |
        3 | |
        2 | |
        1 |W|
           A
        @return:
        """
        piece = Piece(Column.A, 1)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {
            (Column.A, 1): piece,
        }
        expected_squares = []
        assert (
            piece._available_squares_below(square_list, piece_list) == expected_squares
        )

    def test_available_square_below_case5(self):
        """
        8 | |
        7 | |
        6 | |
        5 | |
        4 | |
        3 |W|
        2 |W|
        1 | |
           A
        @return:
        """
        piece = Piece(Column.A, 3)
        other = Piece(Column.A, 2)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {(Column.A, 3): piece, (Column.A, 2): other}
        expected_squares = []
        assert (
            piece._available_squares_below(square_list, piece_list) == expected_squares
        )
