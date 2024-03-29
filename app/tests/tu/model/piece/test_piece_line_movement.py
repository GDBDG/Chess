"""
Tests for available_square in moves classes
"""
from app.src.model.classes.const.color import Color
from app.src.model.classes.const.column import Column
from app.src.model.classes.pieces.piece import Piece
from app.src.model.classes.square import Square
from app.src.model.events.event_getter.square_getter.utils_available_squares_getter import (
    available_squares_on_right,
    available_squares_on_left,
    available_squares_upper,
    available_squares_below,
)
from app.src.model.states.board import Board


class TestMoveAvailableSquare:
    """
    test classes
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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.D, 1),
            Square(Column.E, 1),
        ]
        assert (
            available_squares_on_right(Square(Column.C, 1), board) == expected_squares
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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.D, 1),
            Square(Column.E, 1),
            Square(Column.F, 1),
        ]
        assert (
            available_squares_on_right(Square(Column.C, 1), board) == expected_squares
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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.D, 1),
            Square(Column.E, 1),
            Square(Column.F, 1),
            Square(Column.G, 1),
            Square(Column.H, 1),
        ]
        assert (
            available_squares_on_right(Square(Column.C, 1), board) == expected_squares
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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_on_right(Square(Column.H, 1), board) == expected_squares
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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_on_right(Square(Column.C, 1), board) == expected_squares
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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.E, 1),
            Square(Column.D, 1),
        ]
        assert available_squares_on_left(Square(Column.F, 1), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.E, 1),
            Square(Column.D, 1),
            Square(Column.C, 1),
        ]
        assert available_squares_on_left(Square(Column.F, 1), board) == expected_squares

    def test_available_square_on_left_case3(self):
        """
        1 | | |W| | | | | |
           A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.C, 1): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.B, 1),
            Square(Column.A, 1),
        ]
        assert available_squares_on_left(Square(Column.C, 1), board) == expected_squares

    def test_available_square_on_left_case4(self):
        """
         1 |W| | | | | | | |
            A B C D E F G H
        @return:
        """
        piece_dict = {
            Square(Column.A, 1): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert available_squares_on_left(Square(Column.A, 1), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert available_squares_on_left(Square(Column.D, 1), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.A, 3),
            Square(Column.A, 4),
            Square(Column.A, 5),
        ]
        assert available_squares_upper(Square(Column.A, 2), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.A, 3),
            Square(Column.A, 4),
            Square(Column.A, 5),
            Square(Column.A, 6),
        ]
        assert available_squares_upper(Square(Column.A, 2), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.A, 3),
            Square(Column.A, 4),
            Square(Column.A, 5),
            Square(Column.A, 6),
            Square(Column.A, 7),
            Square(Column.A, 8),
        ]
        assert available_squares_upper(Square(Column.A, 2), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert available_squares_upper(Square(Column.A, 8), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert available_squares_upper(Square(Column.A, 2), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.A, 5),
            Square(Column.A, 4),
            Square(Column.A, 3),
        ]
        assert available_squares_below(Square(Column.A, 6), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.A, 5),
            Square(Column.A, 4),
            Square(Column.A, 3),
            Square(Column.A, 2),
        ]
        assert available_squares_below(Square(Column.A, 6), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.A, 1),
        ]
        assert available_squares_below(Square(Column.A, 2), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert available_squares_below(Square(Column.A, 1), board) == expected_squares

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
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert available_squares_below(Square(Column.A, 3), board) == expected_squares
