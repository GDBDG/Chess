"""
Tests for class Board
"""
import pytest

from app.src.exceptions.invalid_move_error import InvalidMoveError
from app.src.model.chess_board.board import Board
from app.src.model.constantes import SQUARE_NUMBER
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.game_state import GameState
from app.src.model.miscenaleous.move import Move, EmptyMove
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.pieces.king import King
from app.src.model.pieces.queen import Queen
from app.src.model.pieces.rook import Rook


class TestBoard:
    """
    Testing class
    """

    board = Board()

    def test_number_squares(self):
        """
        Assert tha there is the right number of squares in the board
        @return: None
        """
        assert len(self.board.squares.items()) == SQUARE_NUMBER

    def test_available_moves_list(self):
        """
        Test that an initial config return all the 20 moves
        No need to do more tests, they are done in the pieces test
        with the get_available_moves
        @return:
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
        @return:
        """
        move = Move(
            self.board.squares[Column.E, 2],
            self.board.squares[Column.E, 4],
            PieceType.PAWN,
        )
        # with patch.object(Pawn, "apply_move") as mock_move:
        self.board.apply_move(move)
        #     mock_move.assert_called_once_with(
        #         move, self.board.squares, self.board.piece_list,
        #     )
        assert self.board.player == Color.BLACK
        assert self.board.historic == [EmptyMove(), move]

    def test_apply_invalid_move(self):
        """
        Test that an invalid move raises an error
        @return:
        """
        board = Board()
        move = Move(
            board.squares[Column.E, 2],
            board.squares[Column.E, 5],
            PieceType.PAWN,
        )
        with pytest.raises(InvalidMoveError):
            board.apply_move(move)

    def test_apply_invalid_move_wrong_player(self):
        """
        Test that only the right player can play a move
        @return:
        """
        board = Board()
        move = Move(
            board.squares[Column.E, 7],
            board.squares[Column.E, 5],
            PieceType.PAWN,
        )
        with pytest.raises(InvalidMoveError):
            board.apply_move(move)

    def test_draw(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | |R| |
        2 | | | | | | |R| |
        1 | | | | | | | |K|
           A B C D E F G H
        Test that a draw config changes the game status
        @return:
        """
        board = Board()
        board.piece_list = {
            (Column.H, 1): King(Column.H, 1),
            (Column.G, 2): Rook(Column.G, 2, Color.BLACK),
            (Column.G, 3): Rook(Column.G, 3, Color.BLACK),
        }
        board.color = Color.WHITE
        assert not board.available_moves_list()
        assert board.state == GameState.DRAW

    def test_black_win(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | |R| |
        2 | | | | | | |Q| |
        1 | | | | | | | |K|
           A B C D E F G H
        Test that a draw config changes the game status
        @return:
        """
        board = Board()
        board.piece_list = {
            (Column.H, 1): King(Column.H, 1),
            (Column.G, 2): Queen(Column.G, 2, Color.BLACK),
            (Column.G, 3): Rook(Column.G, 3, Color.BLACK),
        }
        board.color = Color.WHITE
        assert not board.available_moves_list()
        assert board.state == GameState.BLACK_WIN

    def test_white_win(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | | | |
        2 | | | | | | |Q| |
        1 | | | | | | | |K|
           A B C D E F G H
        Test that a draw config changes the game status
        @return:
        """
        board = Board()
        board.piece_list = {
            (Column.H, 1): King(Column.H, 1, Color.BLACK),
            (Column.G, 2): Queen(Column.G, 2),
            (Column.G, 3): Rook(Column.G, 3),
        }
        board.player = Color.BLACK
        assert not board.available_moves_list()
        assert board.state == GameState.WHITE_WIN
