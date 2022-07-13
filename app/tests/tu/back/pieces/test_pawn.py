"""
Tests for the pawn
Must test for white and black
"""
from itertools import product

import pytest

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.back.miscenaleous.move import Move
from app.src.back.pieces.pawn import Pawn
from app.src.back.pieces.piece import Piece
from app.src.exceptions.invalid_movement_error import InvalidMovementError


class TestPawn:
    """
    Test class
    """

    square_list = {
        (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
    }

    def test_available_squares_forward(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |B| | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | |W| | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        Test that a pawn can move forward if there is no piece in front of it
        :return:
        """
        white_pawn = Pawn(Column.E, 3)
        white_pawn.has_moved = True
        black_pawn = Pawn(Column.C, 6, Color.BLACK)
        black_pawn.has_moved = True
        piece_list = {
            (Column.E, 3): white_pawn,
            (Column.C, 6): black_pawn,
        }
        expected_white = [self.square_list[Column.E, 4]]
        expected_black = [self.square_list[Column.C, 5]]
        assert (
            white_pawn.available_squares(self.square_list, piece_list) == expected_white
        )
        assert (
            black_pawn.available_squares(self.square_list, piece_list) == expected_black
        )

    def test_available_squares_initial_movement(self):
        """
        8 | | | | | | | | |
        7 | | |B| | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | |W| | | |
        1 | | | | | | | | |
           A B C D E F G H
        Test that a pawn can move of 2 squares for its first movement
        :return:
        """
        white_pawn = Pawn(Column.E, 2)
        black_pawn = Pawn(Column.C, 7, Color.BLACK)
        piece_list = {
            (Column.E, 2): white_pawn,
            (Column.C, 7): black_pawn,
        }
        expected_white = [
            self.square_list[Column.E, 3],
            self.square_list[Column.E, 4],
        ]
        expected_black = [
            self.square_list[Column.C, 6],
            self.square_list[Column.C, 5],
        ]
        assert (
            white_pawn.available_squares(self.square_list, piece_list) == expected_white
        )
        assert (
            black_pawn.available_squares(self.square_list, piece_list) == expected_black
        )

    def test_available_squares_to_capture(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |B| | | | | |
        5 | |w| |w| | | | |
        4 | | | |b| |b| | |
        3 | | | | |W| | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        Test that a pawn can capture a piece
        :return:
        """
        white_pawn = Pawn(Column.E, 3)
        white_pawn.has_moved = True
        other_black1 = Piece(Column.D, 4, Color.BLACK)
        other_black2 = Piece(Column.F, 4, Color.BLACK)
        black_pawn = Pawn(Column.C, 6, Color.BLACK)
        black_pawn.has_moved = True
        other_white1 = Piece(Column.B, 5)
        other_white2 = Piece(Column.D, 5)
        piece_list = {
            (Column.E, 3): white_pawn,
            (Column.C, 6): black_pawn,
            (Column.D, 4): other_black1,
            (Column.F, 4): other_black2,
            (Column.B, 5): other_white1,
            (Column.D, 5): other_white2,
        }
        expected_white = [
            self.square_list[Column.F, 4],
            self.square_list[Column.D, 4],
        ]
        expected_black = [
            self.square_list[Column.D, 5],
            self.square_list[Column.B, 5],
        ]
        assert (
            white_pawn.available_squares_to_capture(self.square_list, piece_list)
            == expected_white
        )
        assert (
            black_pawn.available_squares_to_capture(self.square_list, piece_list)
            == expected_black
        )

    def test_en_passant_available_destination(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |x| | |
        5 | | | | | |B|W| |
        4 | |B|W| | | | | |
        3 | | |x| | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        Test that the correct destination is returned if en passant available
        :return:
        """
        black_pawn = Pawn(Column.B, 4, Color.BLACK)
        white_target_pawn = Pawn(Column.C, 4)
        white_pawn = Pawn(Column.G, 5)
        black_target_pawn = Pawn(Column.F, 5, Color.BLACK)
        last_move_white = Move(
            self.square_list[Column.C, 2],
            self.square_list[Column.C, 4],
            white_target_pawn,
        )
        last_move_black = Move(
            self.square_list[Column.F, 7],
            self.square_list[Column.F, 5],
            black_target_pawn,
        )
        assert (
            black_pawn.en_passant_available_destination(
                self.square_list, last_move_white
            )
            == self.square_list[Column.C, 3]
        )
        assert (
            white_pawn.en_passant_available_destination(
                self.square_list, last_move_black
            )
            == self.square_list[Column.F, 6]
        )

    def test_en_passant_available_destination_none(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |x| | |
        5 | | | | | |B|W| |
        4 | |B|W| | | | | |
        3 | | |x| | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        Test that if the last move does not allow en passant, None is returned
        :return:
        """
        black_pawn = Pawn(Column.B, 4, Color.BLACK)
        white_target_pawn = Pawn(Column.C, 4)
        white_pawn = Pawn(Column.G, 5)
        black_target_pawn = Pawn(Column.F, 5, Color.BLACK)
        last_move_white = Move(
            self.square_list[Column.C, 3],
            self.square_list[Column.C, 4],
            white_target_pawn,
        )
        last_move_black = Move(
            self.square_list[Column.F, 6],
            self.square_list[Column.F, 5],
            black_target_pawn,
        )
        assert (
            black_pawn.en_passant_available_destination(
                self.square_list, last_move_white
            )
            is None
        )
        assert (
            white_pawn.en_passant_available_destination(
                self.square_list, last_move_black
            )
            is None
        )

    def test_en_passant_valid(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |x| | |
        5 | | | | | |B|W| |
        4 | |B|W| | | | | |
        3 | | |x| | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        Test that the en passant move does every thing correctly :
        Moves the pawn
        Capture the opposite pawn
        :return:
        """
        black_pawn = Pawn(Column.B, 4, Color.BLACK)
        white_target_pawn = Pawn(Column.C, 4)
        white_pawn = Pawn(Column.G, 5)
        black_target_pawn = Pawn(Column.F, 5, Color.BLACK)
        piece_list = {
            (Column.B, 4): black_pawn,
            (Column.C, 4): white_target_pawn,
            (Column.G, 5): white_pawn,
            (Column.F, 5): black_target_pawn,
        }
        last_move_white = Move(
            self.square_list[Column.C, 2],
            self.square_list[Column.C, 4],
            white_target_pawn,
        )
        last_move_black = Move(
            self.square_list[Column.F, 7],
            self.square_list[Column.F, 5],
            black_target_pawn,
        )
        black_pawn.en_passant(self.square_list, piece_list, last_move_white)
        assert piece_list[(Column.C, 3)] == black_pawn
        assert (Column.B, 4) not in piece_list
        assert (Column.C, 4) not in piece_list
        assert white_target_pawn not in piece_list.values()
        white_pawn.en_passant(self.square_list, piece_list, last_move_black)
        assert piece_list[(Column.F, 6)] == white_pawn
        assert (Column.F, 5) not in piece_list
        assert (Column.G, 6) not in piece_list
        assert black_target_pawn not in piece_list.values()

    def test_en_passant_invalid(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |x| | |
        5 | | | | | |B|W| |
        4 | |B|W| | | | | |
        3 | | |x| | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        Test that the en passant move does every thing correctly :
        Moves the pawn
        Capture the opposite pawn
        :return:
        """
        black_pawn = Pawn(Column.B, 4, Color.BLACK)
        white_target_pawn = Pawn(Column.C, 4)
        white_pawn = Pawn(Column.G, 5)
        black_target_pawn = Pawn(Column.F, 5, Color.BLACK)
        piece_list = {
            (Column.B, 4): black_pawn,
            (Column.C, 4): white_target_pawn,
            (Column.G, 5): white_pawn,
            (Column.F, 5): black_target_pawn,
        }
        last_move_white = Move(
            self.square_list[Column.C, 3],
            self.square_list[Column.C, 4],
            white_target_pawn,
        )
        last_move_black = Move(
            self.square_list[Column.F, 6],
            self.square_list[Column.F, 5],
            black_target_pawn,
        )
        with pytest.raises(InvalidMovementError):
            black_pawn.en_passant(self.square_list, piece_list, last_move_white)
        with pytest.raises(InvalidMovementError):
            white_pawn.en_passant(self.square_list, piece_list, last_move_black)