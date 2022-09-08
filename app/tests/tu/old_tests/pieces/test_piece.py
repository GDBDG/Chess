"""
Tests for Piece class
"""
from itertools import product
from unittest.mock import MagicMock

import pytest

from app.src.exceptions.invalid_move_error import InvalidMoveError
from app.src.exceptions.invalid_movement_error import InvalidMovementError
from app.src.exceptions.row_error import RowError
from app.src.old_model.chess_board.square import Square
from app.src.old_model.miscenaleous.color import Color
from app.src.old_model.miscenaleous.column import Column
from app.src.old_model.miscenaleous.move import (
    Move,
    EnPassant,
    EmptyMove,
    ShortCastling,
    LongCastling,
    Promotion,
)
from app.src.old_model.miscenaleous.piece_type import PieceType
from app.src.old_model.pieces.bishop import Bishop
from app.src.old_model.pieces.king import King
from app.src.old_model.pieces.piece import Piece
from app.src.old_model.pieces.rook import Rook


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
        @return: None
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
        @return: None
        """
        with pytest.raises(RowError):
            Piece(Column.B, 9)

    def test_available_squares(self):
        """
        test that available squares return correct square_list
        @return: None
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
        @return: None
        """
        piece = self.piece_list[Column.A, 1]
        piece_list = {
            (Column.A, 1): piece,
        }
        piece.move_to(self.square_list[Column.A, 3], self.square_list, piece_list)
        assert piece.row == 3 and piece.column == Column.A
        assert piece.has_moved
        assert (Column.A, 1) not in piece_list
        assert piece_list[Column.A, 3] == piece

    def test_move_to_invalid_destination(self):
        """
        test move_to_destination with incorrect destination (square not in square list,
        or friendly piece in destination)
        @return: None
        """
        piece = self.piece_list[Column.A, 1]
        with pytest.raises(InvalidMovementError):
            piece.move_to(Square(Column.B, 1), self.square_list, self.piece_list)
        with pytest.raises(InvalidMovementError):
            piece.move_to(Square(Column.A, 2), self.square_list, self.piece_list)

    def test_add_square_valid_coordinates(self):
        """
        test _add_square with valid coordinates
        @return: None
        """
        available_squares = []
        Piece._add_square(1, 7, self.square_list, available_squares)
        assert available_squares == [self.square_list[Column.A, 7]]

    def test_add_square_invalid_column(self):
        """
        test _add_square with invalid column
        @return: None
        """
        available_squares = []
        Piece._add_square(9, 7, self.square_list, available_squares)
        assert not available_squares

    def test_add_square_invalid_row(self):
        """
        test _add_square with invalid column
        @return: None
        """
        available_squares = []
        Piece._add_square(1, 9, self.square_list, available_squares)
        assert not available_squares

    def test_is_square_in_check(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |W| | |B| | |
        5 | | | | | | | | |
        4 | | | |X| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        other = Piece(Column.F, 6, Color.BLACK)
        other2 = Piece(Column.C, 6)
        square_list = {
            (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.F, 6): other,
            (Column.C, 6): other2,
        }
        assert Piece.is_square_in_check(
            Color.WHITE, square_list[Column.D, 4], square_list, piece_list
        )

    def test_is_square_not_in_check(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |B| | |
        5 | | | | | | | | |
        4 | | | |X| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        other = Rook(Column.F, 6, Color.BLACK)
        square_list = {
            (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.F, 6): other,
        }
        assert not Piece.is_square_in_check(
            Color.WHITE, square_list[Column.D, 4], square_list, piece_list
        )

    def test_is_square_not_in_check2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | |B| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        other = Rook(Column.D, 4, Color.BLACK)
        square_list = {
            (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): other,
        }
        assert not Piece.is_square_in_check(
            Color.WHITE, square_list[Column.D, 4], square_list, piece_list
        )

    def test_is_in_check(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |W| | |B| | |
        5 | | | | | | | | |
        4 | | | |X| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Piece(Column.D, 4)
        other = Piece(Column.F, 6, Color.BLACK)
        other2 = Piece(Column.C, 6)
        square_list = {
            (col, row): Square(col, 1) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 6): other,
            (Column.C, 6): other2,
        }
        assert piece.is_in_check(square_list, piece_list)

    def test_is_not_in_check(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |B| | |
        5 | | | | | | | | |
        4 | | | |X| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Piece(Column.D, 4)
        other = Rook(Column.F, 6, Color.BLACK)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.D, 4): piece,
            (Column.F, 6): other,
        }
        assert not piece.is_in_check(square_list, piece_list)

    def test_is_not_in_check2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |B| | |
        5 | | | | |W| | | |
        4 | | | |X| | | | |
        3 | | | | | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return:
        """
        piece = Piece(Column.D, 4)
        other = Bishop(Column.F, 6, Color.BLACK)
        white = Piece(Column.E, 5)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {(Column.D, 4): piece, (Column.F, 6): other, (Column.E, 5): white}
        assert not piece.is_in_check(square_list, piece_list)

    def test_apply_valid_move(self):
        """
        Test that a valid move can be played
        @return:
        """
        piece = Piece(Column.A, 1)
        piece.move_to = MagicMock()
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.A, 1): piece,
        }
        move = Move(
            square_list[Column.A, 1],
            square_list[Column.A, 2],
            PieceType.PIECE,
        )
        last_move = EmptyMove()
        piece._apply_move_no_legal_verification(
            move, square_list, piece_list, last_move
        )
        piece.move_to.assert_called_once_with(move.destination, square_list, piece_list)

    def test_apply_invalid_move(self):
        """
        Test that an invalid_move raises an error
        @return:
        """
        piece = Piece(Column.A, 1)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.A, 1): piece,
        }
        move = Move(
            square_list[Column.A, 1],
            square_list[Column.A, 1],
            PieceType.PIECE,
        )
        with pytest.raises(InvalidMoveError):
            piece._apply_move_no_legal_verification(
                move, square_list, piece_list, EmptyMove()
            )

    def test_apply_invalid_move2(self):
        """
        Test that a specific move (EnPassant, Castling, ...) raises an error
        @return:
        """
        piece = Piece(Column.A, 1)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.A, 1): piece,
        }
        move = EmptyMove()
        with pytest.raises(InvalidMoveError):
            piece._apply_move_no_legal_verification(
                move, square_list, piece_list, EmptyMove()
            )
        move = ShortCastling(
            square_list[Column.A, 1],
            square_list[Column.A, 2],
        )
        with pytest.raises(InvalidMoveError):
            piece._apply_move_no_legal_verification(
                move, square_list, piece_list, EmptyMove()
            )
        move = LongCastling(
            square_list[Column.A, 1],
            square_list[Column.A, 2],
        )
        with pytest.raises(InvalidMoveError):
            piece._apply_move_no_legal_verification(
                move, square_list, piece_list, EmptyMove()
            )
        move = EnPassant(
            square_list[Column.A, 1],
            square_list[Column.A, 2],
        )
        with pytest.raises(InvalidMoveError):
            piece._apply_move_no_legal_verification(
                move, square_list, piece_list, EmptyMove()
            )
        move = Promotion(
            square_list[Column.A, 1], square_list[Column.A, 2], PieceType.PIECE
        )
        with pytest.raises(InvalidMoveError):
            piece._apply_move_no_legal_verification(
                move, square_list, piece_list, EmptyMove()
            )

    def test_is_move_legal(self):
        """
        Test that a move is legal
         8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | |W| | |
        1 | | | | |K| | |B|
           A B C D E F G H
        @return:
        """
        king = King(Column.E, 1)
        white_piece = Piece(Column.F, 2)
        other = Rook(Column.H, 1, Color.BLACK)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.E, 1): king,
            (Column.F, 2): white_piece,
            (Column.H, 1): other,
        }
        moves_to_test = [
            Move(
                square_list[Column.F, 2],
                square_list[Column.F, 1],
                PieceType.PIECE,
            ),
            Move(
                square_list[Column.F, 2],
                square_list[Column.G, 1],
                PieceType.PIECE,
            ),
            Move(
                square_list[Column.F, 2],
                square_list[Column.H, 1],
                PieceType.PIECE,
            ),
        ]
        last_move = EmptyMove()
        for move in moves_to_test:
            assert white_piece.is_move_legal(move, last_move, square_list, piece_list)

    def test_only_legal_in_available_moves(self):
        """
        Assert that a move is legal
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | |W| | |
        1 | | | | |K| | |B|
           A B C D E F G H
        @return:
        """
        king = King(Column.E, 1)
        white_piece = Piece(Column.F, 2)
        other = Rook(Column.H, 1, Color.BLACK)
        square_list = {
            (col, row): Square(col, row) for col, row in product(Column, range(1, 9))
        }
        piece_list = {
            (Column.E, 1): king,
            (Column.F, 2): white_piece,
            (Column.H, 1): other,
        }
        expected_moves = {
            Move(
                square_list[Column.F, 2],
                square_list[Column.F, 1],
                PieceType.PIECE,
            ),
            Move(
                square_list[Column.F, 2],
                square_list[Column.G, 1],
                PieceType.PIECE,
            ),
            Move(
                square_list[Column.F, 2],
                square_list[Column.H, 1],
                PieceType.PIECE,
            ),
        }
        assert (
            set(white_piece.available_moves(square_list, piece_list, EmptyMove()))
            == expected_moves
        )
        expected_moves = {
            Move(
                square_list[Column.E, 1],
                square_list[Column.E, 2],
                PieceType.KING,
            ),
            Move(
                square_list[Column.E, 1],
                square_list[Column.D, 2],
                PieceType.KING,
            ),
        }
        assert (
            set(king.available_moves(square_list, piece_list, EmptyMove()))
            == expected_moves
        )
