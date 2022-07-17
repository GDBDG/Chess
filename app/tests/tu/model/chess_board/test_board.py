"""
Tests for class Board
"""
from app.src.model.chess_board.board import Board
from app.src.model.constantes import SQUARE_NUMBER
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.move import Move
from app.src.model.miscenaleous.piece_type import PieceType


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
