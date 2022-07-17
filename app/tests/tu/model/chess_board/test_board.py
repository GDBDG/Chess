"""
Tests for class Board
"""
from unittest.mock import patch

from app.src.model.chess_board.board import Board
from app.src.model.constantes import SQUARE_NUMBER
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.move import Move
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.pieces.piece import Piece


class TestBoard:
    """
    Testing class
    """

    board = Board()

    def test_number_squares(self):
        """
        Assert tha there is the right number of squares in the board
        :return: None
        """
        assert len(self.board.squares.items()) == SQUARE_NUMBER

    def test_available_moves_list(self):
        """
        Test that an initial config return all the 20 moves
        No need to do more tests, they are done in the pieces test
        with the get_available_moves
        :return:
        """
        square_list = self.board.squares
        expected_moves = {
            Move(
                square_list[Column.A, 2],
                square_list[Column.A, 3],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.A, 2],
                square_list[Column.A, 4],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.B, 2],
                square_list[Column.B, 3],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.B, 2],
                square_list[Column.B, 4],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.C, 2],
                square_list[Column.C, 3],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.C, 2],
                square_list[Column.C, 4],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.D, 2],
                square_list[Column.D, 3],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.D, 2],
                square_list[Column.D, 4],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.E, 2],
                square_list[Column.E, 3],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.E, 2],
                square_list[Column.E, 4],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.F, 2],
                square_list[Column.F, 3],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.F, 2],
                square_list[Column.F, 4],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.G, 2],
                square_list[Column.G, 3],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.G, 2],
                square_list[Column.G, 4],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.H, 2],
                square_list[Column.H, 3],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.H, 2],
                square_list[Column.H, 4],
                PieceType.PAWN,
            ),
            Move(
                square_list[Column.B, 1],
                square_list[Column.A, 3],
                PieceType.KNIGHT,
            ),
            Move(
                square_list[Column.B, 1],
                square_list[Column.C, 3],
                PieceType.KNIGHT,
            ),
            Move(
                square_list[Column.G, 1],
                square_list[Column.F, 3],
                PieceType.KNIGHT,
            ),
            Move(
                square_list[Column.G, 1],
                square_list[Column.H, 3],
                PieceType.KNIGHT,
            ),
        }
        assert set(self.board.available_moves_list()) == expected_moves

    def test_apply_move(self):
        """
        Test that a move applied changes the state of the player, and
        call apply_move for the piece
        :return:
        """
        move = Move(
            self.board.squares[Column.E, 2],
            self.board.squares[Column.E, 4],
            PieceType.PAWN,
        )
        with patch.object(Piece, "apply_move") as mock_move:
            self.board.apply_move(move)
            mock_move.assert_called_once_with(move, self.board.squares, self.board.piece_list)
        assert self.board.player == Color.BLACK
