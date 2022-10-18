"""
Tests for piece (diagonal movements)
"""
from app.src.model.available_move_getter.available_squares_getter import (
    available_squares_diagonal_right_up,
    available_squares_diagonal_right_down,
    available_squares_diagonal_left_up,
    available_squares_diagonal_left_down,
)
from app.src.model.game.board import Board
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.pieces.piece import Piece


class TestPiece:
    """
    Test class
    """

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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.F, 6): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.E, 5),
        ]
        assert (
            available_squares_diagonal_right_up(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.F, 6): Piece(Color.BLACK),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.E, 5),
            Square(Column.F, 6),
        ]
        assert (
            available_squares_diagonal_right_up(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 5): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.E, 6),
            Square(Column.F, 7),
            Square(Column.G, 8),
        ]
        assert (
            available_squares_diagonal_right_up(Square(Column.D, 5), board)
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
        piece_dict = {
            Square(Column.H, 7): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_diagonal_right_up(Square(Column.H, 7), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.E, 5): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_diagonal_right_up(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.F, 2): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.E, 3),
        ]
        assert (
            available_squares_diagonal_right_down(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.F, 2): Piece(Color.BLACK),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.E, 3),
            Square(Column.F, 2),
        ]
        assert (
            available_squares_diagonal_right_down(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.E, 3),
            Square(Column.F, 2),
            Square(Column.G, 1),
        ]
        assert (
            available_squares_diagonal_right_down(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.F, 1): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_diagonal_right_down(Square(Column.F, 1), board)
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
        piece_dict = {
            Square(Column.D, 3): Piece(Color.WHITE),
            Square(Column.E, 2): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_diagonal_right_down(Square(Column.D, 3), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.B, 6): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.C, 5),
        ]
        assert (
            available_squares_diagonal_left_up(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.B, 6): Piece(Color.BLACK),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.C, 5),
            Square(Column.B, 6),
        ]
        assert (
            available_squares_diagonal_left_up(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.C, 5),
            Square(Column.B, 6),
            Square(Column.A, 7),
        ]
        assert (
            available_squares_diagonal_left_up(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.A, 7): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_diagonal_left_up(Square(Column.A, 7), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.C, 5): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_diagonal_left_up(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.B, 2): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.C, 3),
        ]
        assert (
            available_squares_diagonal_left_down(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.B, 2): Piece(Color.BLACK),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.C, 3),
            Square(Column.B, 2),
        ]
        assert (
            available_squares_diagonal_left_down(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = [
            Square(Column.C, 3),
            Square(Column.B, 2),
            Square(Column.A, 1),
        ]
        assert (
            available_squares_diagonal_left_down(Square(Column.D, 4), board)
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
        piece_dict = {
            Square(Column.A, 2): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_diagonal_left_down(Square(Column.A, 2), board)
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
        piece_dict = {
            Square(Column.D, 4): Piece(Color.WHITE),
            Square(Column.C, 3): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_squares = []
        assert (
            available_squares_diagonal_left_down(Square(Column.D, 4), board)
            == expected_squares
        )
