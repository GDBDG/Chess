"""
Tests for Piece class
"""
from itertools import product

import pytest

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.back.pieces.piece import Piece
from app.src.back.pieces.rook import Rook
from app.src.exceptions.row_error import RowError
from app.src.exceptions.unavailable_square_error import UnavailableSquareError


class TestPiece:
    """
    test class
    """

    piece_list = {
        (Column.A, 1): Piece(Column.A, 1),
        (Column.A, 2): Piece(Column.A, 2),
        (Column.A, 3): Piece(Column.A, 3, Color.BLACK),
    }
    square_list = {(Column.A, i): Square(Column.A, i) for i in range(1, 9)}

    def test_valid_init(self):
        """
        Test all valid instantiation
        :return: None
        """
        for row, column, color in product(range(1, 9), Column, Color):
            piece = Piece(column, row, color)
            assert piece.column == column
            assert piece.row == row
            assert piece.color == color

    def test_invalid_instantiation(self):
        """
        Test if an incorrect row is given
        assert RowError is raised
        :return: None
        """
        with pytest.raises(RowError):
            Piece(Column.B, 9)

    def test_available_squares(self):
        """
        test that available squares return correct square_list
        :return: None
        """
        expected_list = [self.square_list[Column.A, i] for i in range(3, 9)]
        assert (
                self.piece_list[Column.A, 1].available_squares(
                    self.square_list, self.piece_list
                )
                == expected_list
        )

    def test_move_to_valid_destination(self):
        """
        Test move_to_destination, when a correct destination is provided
        :return: None
        """
        piece = self.piece_list[Column.A, 1]
        piece.move_to(self.square_list[Column.A, 3], self.square_list, self.piece_list)
        assert piece.row == 3 and piece.column == Column.A

    def test_move_to_invalid_destination(self):
        """
        test move_to_destination with incorrect destination (square not in square list,
        or friendly piece in destination)
        :return: None
        """
        piece = self.piece_list[Column.A, 1]
        with pytest.raises(UnavailableSquareError):
            piece.move_to(Square(Column.B, 1), self.square_list, self.piece_list)
        with pytest.raises(UnavailableSquareError):
            piece.move_to(Square(Column.A, 2), self.square_list, self.piece_list)

    def test_available_square_on_right_case1(self):
        """
        1 | | |W| | |W| | |
           A B C D E F G H
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
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
        :return:
        """
        piece = Piece(Column.A, 3)
        other = Piece(Column.A, 2)
        square_list = {(Column.A, row): Square(Column.A, row) for row in range(1, 9)}
        piece_list = {(Column.A, 3): piece, (Column.A, 2): other}
        expected_squares = []
        assert (
                piece._available_squares_below(square_list, piece_list) == expected_squares
        )

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.F, 6)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 6): other1,
        }
        expected_squares = [
            square_list[Column.E, 5],
        ]
        assert piece._available_squares_diagonal_right_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.F, 6, Color.BLACK)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 6): other1,
        }
        expected_squares = [
            square_list[Column.E, 5],
            square_list[Column.F, 6],
        ]
        assert piece._available_squares_diagonal_right_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 5)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 5): piece,
        }
        expected_squares = [
            square_list[Column.E, 6],
            square_list[Column.F, 7],
            square_list[Column.G, 8],
        ]
        assert piece._available_squares_diagonal_right_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.H, 7)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.H, 7): piece,
        }
        expected_squares = []
        assert piece._available_squares_diagonal_right_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.E, 5)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.E, 5): other1,
        }
        expected_squares = []
        assert piece._available_squares_diagonal_right_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.F, 2)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 2): other1,
        }
        expected_squares = [
            square_list[Column.E, 3],
        ]
        assert piece._available_squares_diagonal_right_down(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.F, 2, Color.BLACK)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 2): other1,
        }
        expected_squares = [
            square_list[Column.E, 3],
            square_list[Column.F, 2],
        ]
        assert piece._available_squares_diagonal_right_down(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = [
            square_list[Column.E, 3],
            square_list[Column.F, 2],
            square_list[Column.G, 1],

        ]
        assert piece._available_squares_diagonal_right_down(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.F, 1)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.F, 1): piece,
        }
        expected_squares = []
        assert piece._available_squares_diagonal_right_down(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 3)
        other = Piece(Column.E, 2)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.F, 1): piece,
            (Column.E, 2): other,
        }
        expected_squares = []
        assert piece._available_squares_diagonal_right_down(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.B, 6)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.B, 6): other1,
        }
        expected_squares = [
            square_list[Column.C, 5],
        ]
        assert piece._available_squares_diagonal_left_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.B, 6, Color.BLACK)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.B, 6): other1,
        }
        expected_squares = [
            square_list[Column.C, 5],
            square_list[Column.B, 6],
        ]
        assert piece._available_squares_diagonal_left_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = [
            square_list[Column.C, 5],
            square_list[Column.B, 6],
            square_list[Column.A, 7],

        ]
        assert piece._available_squares_diagonal_left_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.A, 7)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = []
        assert piece._available_squares_diagonal_left_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other = Piece(Column.C, 5)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.C, 5): other,
        }
        expected_squares = []
        assert piece._available_squares_diagonal_left_up(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.B, 2)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.B, 2): other1,
        }
        expected_squares = [
            square_list[Column.C, 3],
        ]
        assert piece._available_squares_diagonal_left_down(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.B, 2, Color.BLACK)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.B, 2): other1,
        }
        expected_squares = [
            square_list[Column.C, 3],
            square_list[Column.B, 2],
        ]
        assert piece._available_squares_diagonal_left_down(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = [
            square_list[Column.C, 3],
            square_list[Column.B, 2],
            square_list[Column.A, 1],

        ]
        assert piece._available_squares_diagonal_left_down(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.A, 2)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
        }
        expected_squares = []
        assert piece._available_squares_diagonal_left_down(square_list, piece_list) == expected_squares

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
        :return:
        """
        piece = Rook(Column.D, 4)
        other1 = Piece(Column.C, 3)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.C, 3): other1,
        }
        expected_squares = []
        assert piece._available_squares_diagonal_left_down(square_list, piece_list) == expected_squares
