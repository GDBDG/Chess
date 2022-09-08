"""
Tests for the draw rules:
- stalemate (no legal move available)
- dead position
"""
import pytest

from app.src.old_model.chess_board.board import Board
from app.src.old_model.miscenaleous.color import Color
from app.src.old_model.miscenaleous.column import Column
from app.src.old_model.miscenaleous.game_state import GameState
from app.src.old_model.miscenaleous.move import Move
from app.src.old_model.miscenaleous.piece_type import PieceType
from app.src.old_model.pieces.bishop import Bishop
from app.src.old_model.pieces.king import King
from app.src.old_model.pieces.knight import Knight
from app.src.old_model.pieces.rook import Rook


class TestDraw:
    """
    Testing class
    """

    def test_stalemate(self):
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

    @pytest.mark.skip(reason="not yet implemented")
    def test_dead_position1(self):
        """
        Test that a dead position leads to a draw.
        1 king VS king
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | |B| |
        2 | | | | | | | | |
        1 | | | | | | | |W|
           A B C D E F G H
        @return:
        """
        board = Board()
        board.piece_list = {
            (Column.H, 1): King(Column.H, 1),
            (Column.G, 3): King(Column.G, 3, Color.BLACK),
        }
        board.piece_list[Column.H, 1].has_moved = True
        assert board.state == GameState.DRAW

    @pytest.mark.skip(reason="not yet implemented")
    def test_dead_position2(self):
        """
        Test that a dead position leads to a draw.
        1 king VS king and bishop
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | |b| | |B| |
        2 | | | | | | | | |
        1 | | | | | | | |W|
           A B C D E F G H
        @return:
        """
        board = Board()
        board.piece_list = {
            (Column.H, 1): King(Column.H, 1),
            (Column.G, 3): King(Column.G, 3, Color.BLACK),
            (Column.D, 3): Bishop(Column.D, 3),
        }
        board.piece_list[Column.H, 1].has_moved = True
        assert board.state == GameState.DRAW

    @pytest.mark.skip(reason="not yet implemented")
    def test_dead_position3(self):
        """
        Test that a dead position leads to a draw.
        1 king VS king and knight
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | |b| | |B| |
        2 | | | | | | | | |
        1 | | | | | | | |W|
           A B C D E F G H
        @return:
        """
        board = Board()
        board.piece_list = {
            (Column.H, 1): King(Column.H, 1),
            (Column.G, 3): King(Column.G, 3, Color.BLACK),
            (Column.D, 3): Knight(Column.D, 3),
        }
        board.piece_list[Column.H, 1].has_moved = True
        assert board.state == GameState.DRAW

    @pytest.mark.skip(reason="not yet implemented")
    def test_dead_position4(self):
        """
        Test that a dead position leads to a draw.
        1 king and bishop VS king and bishop, both on same color
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | |b| | |B| |
        2 | | | | | | | | |
        1 | | | | | | | |W|
           A B C D E F G H
        @return:
        """
        board = Board()
        board.piece_list = {
            (Column.H, 1): King(Column.H, 1),
            (Column.G, 3): King(Column.G, 3, Color.BLACK),
            (Column.D, 3): Knight(Column.D, 3),
            (Column.D, 5): Knight(Column.D, 5, Color.BLACK),
        }
        board.piece_list[Column.H, 1].has_moved = True
        assert board.state == GameState.DRAW

    @pytest.mark.skip(reason="not yet implemented")
    def test_threefold_repetition_rule(self):
        """
        Test the threefold repetition rule
        8 |R| | | | | | | |
        7 |r| | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 | | | | | | | | |
        3 | | | | | | |k| |
        2 | | | | | | | | |
        1 | | | | | | | |K|
           A B C D E F G H
        @return:
        """
        board = Board()
        board.piece_list = {
            (Column.H, 1): King(Column.H, 1),
            (Column.G, 3): King(Column.G, 3, Color.BLACK),
            (Column.A, 8): Rook(Column.A, 8),
            (Column.A, 7): Rook(Column.A, 7, Color.BLACK),
        }
        board.piece_list[Column.H, 1].has_moved = True
        move_list = [
            Move(board.squares[Column.A, 8], board.squares[Column.H, 8], PieceType.ROOK),
            Move(board.squares[Column.A, 7], board.squares[Column.G, 7], PieceType.ROOK),
            Move(board.squares[Column.H, 8], board.squares[Column.D, 8], PieceType.ROOK),
            Move(board.squares[Column.G, 7], board.squares[Column.A, 7], PieceType.ROOK),
            Move(board.squares[Column.D, 8], board.squares[Column.A, 8], PieceType.ROOK),  # 2
            Move(board.squares[Column.G, 3], board.squares[Column.G, 4], PieceType.KING),
            Move(board.squares[Column.H, 1], board.squares[Column.G, 1], PieceType.KING),
            Move(board.squares[Column.G, 4], board.squares[Column.G, 3], PieceType.KING),
            Move(board.squares[Column.G, 1], board.squares[Column.H, 1], PieceType.KING),  # 3
        ]
        list(map(board.apply_move, move_list))
        assert board.state == GameState.DRAW

    @pytest.mark.skip(reason="not yet implemented")
    def test_fifty_move(self):
        """
        Test the fifty move rule.
        @return:
        """
