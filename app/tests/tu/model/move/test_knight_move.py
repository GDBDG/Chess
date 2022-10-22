"""
test knight
"""
from app.src.model.classes.pieces.knight import Knight
from app.src.model.classes.pieces.piece import Piece
from app.src.model.events.moves.knight_move import KnightMove
from app.src.model.game.board import Board
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.utils import square_available_moves_no_castling


class TestKnight:
    """
    Class test
    """

    def test_available_moves1(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |x| |x| | | |
        5 | |x| | | |x| | |
        4 | | | |K| | | | |
        3 | |x| | | |x| | |
        2 | | |x| |x| | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return: None
        """
        piece_dict = {
            Square(Column.D, 4): Knight(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_moves = [
            KnightMove(Square(Column.D, 4), Square(Column.C, 6)),
            KnightMove(Square(Column.D, 4), Square(Column.E, 6)),
            KnightMove(Square(Column.D, 4), Square(Column.C, 2)),
            KnightMove(Square(Column.D, 4), Square(Column.E, 2)),
            KnightMove(Square(Column.D, 4), Square(Column.F, 3)),
            KnightMove(Square(Column.D, 4), Square(Column.F, 5)),
            KnightMove(Square(Column.D, 4), Square(Column.B, 3)),
            KnightMove(Square(Column.D, 4), Square(Column.B, 5)),
        ]
        assert (
            square_available_moves_no_castling(Square(Column.D, 4), board)
            == expected_moves
        )

    def test_available_moves2(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | | | | |
        5 | | | | | | | | |
        4 |x| |x| | | | | |
        3 | | | |x| | | | |
        2 | |K| | | | | | |
        1 | | | |x| | | | |
           A B C D E F G H
        @return: None
        """
        piece_dict = {
            Square(Column.B, 2): Knight(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_moves = [
            KnightMove(Square(Column.B, 2), Square(Column.A, 4)),
            KnightMove(Square(Column.B, 2), Square(Column.C, 4)),
            KnightMove(Square(Column.B, 2), Square(Column.D, 1)),
            KnightMove(Square(Column.B, 2), Square(Column.D, 3)),
        ]

        assert (
            square_available_moves_no_castling(Square(Column.B, 2), board)
            == expected_moves
        )

    def test_available_moves3(self):
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | |x| |W| | | |
        5 | |W| | | |B| | |
        4 | | | |K| | | | |
        3 | |x| | | |x| | |
        2 | | |x| |B| | | |
        1 | | | | | | | | |
           A B C D E F G H
        @return: None
        """
        piece_dict = {
            Square(Column.D, 4): Knight(Color.WHITE),
            Square(Column.E, 6): Piece(Color.WHITE),
            Square(Column.F, 5): Piece(Color.BLACK),
            Square(Column.E, 2): Piece(Color.BLACK),
            Square(Column.B, 5): Piece(Color.WHITE),
        }
        board = Board()
        board.piece_dict = piece_dict
        expected_moves = [
            KnightMove(Square(Column.D, 4), Square(Column.C, 6)),
            KnightMove(Square(Column.D, 4), Square(Column.C, 2)),
            KnightMove(Square(Column.D, 4), Square(Column.E, 2)),
            KnightMove(Square(Column.D, 4), Square(Column.F, 3)),
            KnightMove(Square(Column.D, 4), Square(Column.F, 5)),
            KnightMove(Square(Column.D, 4), Square(Column.B, 3)),
        ]
        assert (
            square_available_moves_no_castling(Square(Column.D, 4), board)
            == expected_moves
        )
