"""
Queen
"""
from app.src.model.available_move_getter.available_squares_getter import _available_squares_on_right, \
    _available_squares_on_left, _available_squares_upper, _available_squares_below, available_squares_diagonal_right_up, \
    available_squares_diagonal_right_down, available_squares_diagonal_left_up, available_squares_diagonal_left_down
from app.src.model.classes.pieces.piece import Piece
from app.src.model.events.moves.queen_move import QueenMove
from app.src.model.game.board import Board
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color


class Queen(Piece):
    """
    Queen classes
    """
    move = QueenMove

    @staticmethod
    def available_squares(origin: Square, board: Board) -> [Square]:
        """
            A queen moves in line and diagonal, and can't go threw another piece,
            but can take a piece with a different color.
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
        # diagonal right up squares
        available_squares.extend(
            available_squares_diagonal_right_up(
                origin,
                board
            )
        )
        # diagonal right down squares
        available_squares.extend(
            available_squares_diagonal_right_down(
                origin,
                board
            )
        )
        # diagonal left up squares
        available_squares.extend(
            available_squares_diagonal_left_up(
                origin,
                board
            )
        )
        # diagonal left down squares
        available_squares.extend(
            available_squares_diagonal_left_down(
                origin,
                board
            )
        )
        return available_squares

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1101 or 0101
        """
        return 0b1101 if self.color == Color.WHITE else 0b0101

    def __repr__(self):
        return "Q" if self.color == Color.WHITE else "q"
