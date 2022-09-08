"""
Tests for piece class
(Tests for movement checks in line
"""
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.move.move import Move
from app.src.model.pieces.piece import Piece


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
        piece_dict = {
            Square(Column.C, 1): Piece(Color.WHITE),
            Square(Column.F, 1): Piece(Color.WHITE),
        }
        expected_squares = [
            Square(Column.D, 1),
            Square(Column.E, 1),
        ]
        assert (
            Move._available_squares_on_right(Square(Column.C, 1), piece_dict)
            == expected_squares
        )

    def test_available_square_on_right_case2(self):
        """
        1 | | |W| | |B| | |
           A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.C, 1): Piece(Color.WHITE),
            Square(Column.F, 1): Piece(Color.BLACK),
        }
        expected_squares = [
            Square(Column.D, 1),
            Square(Column.E, 1),
            Square(Column.F, 1),
        ]
        assert (
            Move._available_squares_on_right(Square(Column.C, 1), piece_dict)
            == expected_squares
        )

    def test_available_square_on_right_case3(self):
        """
        1 | | |W| | | | | |
           A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.C, 1): Piece(Color.WHITE),
        }
        expected_squares = [
            Square(Column.D, 1),
            Square(Column.E, 1),
            Square(Column.F, 1),
            Square(Column.G, 1),
            Square(Column.H, 1),
        ]
        assert (
            Move._available_squares_on_right(Square(Column.C, 1), piece_dict)
            == expected_squares
        )

    def test_available_square_on_right_case4(self):
        """
         1 | | | | | | | |W|
            A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.H, 1): Piece(Color.WHITE),
        }
        expected_squares = []
        assert (
            Move._available_squares_on_right(Square(Column.H, 1), piece_dict)
            == expected_squares
        )

    def test_available_square_on_right_case5(self):
        """
        1 | | |W|W| | | | |
           A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.C, 1): Piece(Color.WHITE),
            Square(Column.D, 1): Piece(Color.WHITE),
        }
        expected_squares = []
        assert (
            Move._available_squares_on_right(Square(Column.C, 1), piece_dict)
            == expected_squares
        )

    def test_available_square_on_left_case1(self):
        """
        1 | | |W| | |W| | |
           A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.C, 1): Piece(Color.WHITE),
            Square(Column.F, 1): Piece(Color.WHITE),
        }
        expected_squares = [
            Square(Column.E, 1),
            Square(Column.D, 1),
        ]
        assert (
            Move._available_squares_on_left(Square(Column.F, 1), piece_dict)
            == expected_squares
        )

    def test_available_square_on_left_case2(self):
        """
        1 | | |W| | |B| | |
           A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.C, 1): Piece(Color.WHITE),
            Square(Column.F, 1): Piece(Color.BLACK),
        }
        expected_squares = [
            Square(Column.E, 1),
            Square(Column.D, 1),
            Square(Column.C, 1),
        ]
        assert (
            Move._available_squares_on_left(Square(Column.F, 1), piece_dict)
            == expected_squares
        )

    def test_available_square_on_left_case3(self):
        """
        1 | | |W| | | | | |
           A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.C, 1): Piece(Color.WHITE),
        }
        expected_squares = [
            Square(Column.B, 1),
            Square(Column.A, 1),
        ]
        assert (
            Move._available_squares_on_left(Square(Column.C, 1), piece_dict)
            == expected_squares
        )

    def test_available_square_on_left_case4(self):
        """
         1 |W| | | | | | | |
            A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.A, 1): Piece(Color.WHITE),
        }
        expected_squares = []
        assert (
            Move._available_squares_on_left(Square(Column.A, 1), piece_dict)
            == expected_squares
        )

    def test_available_square_on_left_case5(self):
        """
        1 | | |W|W| | | | |
           A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.C, 1): Piece(Color.WHITE),
            Square(Column.D, 1): Piece(Color.WHITE),
        }
        expected_squares = []
        assert (
            Move._available_squares_on_left(Square(Column.D, 1), piece_dict)
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
        piece_dict = {
            Square(Column.A, 2): Piece(Color.WHITE),
            Square(Column.A, 6): Piece(Color.WHITE),
        }
        expected_squares = [
            Square(Column.A, 3),
            Square(Column.A, 4),
            Square(Column.A, 5),
        ]
        assert (
            Move._available_squares_upper(Square(Column.A, 2), piece_dict)
            == expected_squares
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
        piece_dict = {
            Square(Column.A, 2): Piece(Color.WHITE),
            Square(Column.A, 6): Piece(Color.BLACK),
        }
        expected_squares = [
            Square(Column.A, 3),
            Square(Column.A, 4),
            Square(Column.A, 5),
            Square(Column.A, 6),
        ]
        assert (
            Move._available_squares_upper(Square(Column.A, 2), piece_dict)
            == expected_squares
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
        piece_dict = {
            Square(Column.A, 2): Piece(Color.WHITE),
        }
        expected_squares = [
            Square(Column.A, 3),
            Square(Column.A, 4),
            Square(Column.A, 5),
            Square(Column.A, 6),
            Square(Column.A, 7),
            Square(Column.A, 8),
        ]
        assert (
            Move._available_squares_upper(Square(Column.A, 2), piece_dict)
            == expected_squares
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
        piece_dict = {
            Square(Column.A, 8): Piece(Color.WHITE),
        }
        expected_squares = []
        assert (
            Move._available_squares_upper(Square(Column.A, 8), piece_dict)
            == expected_squares
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
        piece_dict = {
            Square(Column.A, 2): Piece(Color.WHITE),
            Square(Column.A, 3): Piece(Color.WHITE),
        }
        expected_squares = []
        assert (
            Move._available_squares_upper(Square(Column.A, 2), piece_dict)
            == expected_squares
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
        piece_dict = {
            Square(Column.A, 2): Piece(Color.WHITE),
            Square(Column.A, 6): Piece(Color.WHITE),
        }
        expected_squares = [
            Square(Column.A, 5),
            Square(Column.A, 4),
            Square(Column.A, 3),
        ]
        assert (
            Move._available_squares_below(Square(Column.A, 6), piece_dict)
            == expected_squares
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
        piece_dict = {
            Square(Column.A, 2): Piece(Color.WHITE),
            Square(Column.A, 6): Piece(Color.BLACK),
        }
        expected_squares = [
            Square(Column.A, 5),
            Square(Column.A, 4),
            Square(Column.A, 3),
            Square(Column.A, 2),
        ]
        assert (
            Move._available_squares_below(Square(Column.A, 6), piece_dict)
            == expected_squares
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
        piece_dict = {
            Square(Column.A, 2): Piece(Color.WHITE),
        }
        expected_squares = [
            Square(Column.A, 1),
        ]
        assert (
            Move._available_squares_below(Square(Column.A, 2), piece_dict)
            == expected_squares
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
        piece_dict = {
            Square(Column.A, 1): Piece(Color.WHITE),
        }
        expected_squares = []
        assert (
            Move._available_squares_below(Square(Column.A, 1), piece_dict)
            == expected_squares
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
        piece_dict = {
            Square(Column.A, 2): Piece(Color.WHITE),
            Square(Column.A, 3): Piece(Color.WHITE),
        }
        expected_squares = []
        assert (
            Move._available_squares_below(Square(Column.A, 3), piece_dict)
            == expected_squares
        )
