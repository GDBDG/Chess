"""
Rook
"""
from app.src.model.available_move_getter.available_squares_getter import _available_squares_on_right, \
    _available_squares_on_left, _available_squares_upper, _available_squares_below
from app.src.model.game.board import Board
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.move.rook_move import RookMove
from app.src.model.pieces.piece import Piece


class Rook(Piece):
    """
    Rook class
    """
    move = RookMove

    @staticmethod
    def available_squares(origin: Square, board: Board) -> [Square]:
        """
        A rook move in line, and can't go threw another piece,
        but can take a piece with a different color.
        @param board:
        @return: list of reachable squares
        """
        available_squares: list[Square] = []
        # right squares
        available_squares.extend(
            _available_squares_on_right(
                origin,
                board
            )
        )
        # left squares
        available_squares.extend(
            _available_squares_on_left(
                origin,
                board
            )
        )
        # up squares
        available_squares.extend(
            _available_squares_upper(
                origin,
                board
            )
        )
        # down squares
        available_squares.extend(
            _available_squares_below(
                origin,
                board
            )
        )
        return available_squares

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1110 or 0100
        """
        return 0b1110 if self.color == Color.WHITE else 0b0110

    def __repr__(self):
        return "R" if self.color == Color.WHITE else "r"
