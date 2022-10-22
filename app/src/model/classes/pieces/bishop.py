"""
Bishop
"""
from app.src.model.available_move_getter.available_squares_getter import available_squares_diagonal_right_up, \
    available_squares_diagonal_right_down, available_squares_diagonal_left_up, available_squares_diagonal_left_down
from app.src.model.classes.const.color import Color
from app.src.model.classes.pieces.piece import Piece
from app.src.model.classes.square import Square
from app.src.model.events.moves.bishop_move import BishopMove
from app.src.model.game.board import Board


class Bishop(Piece):
    """
    Bishop classes
    """
    move = BishopMove

    @staticmethod
    def available_squares(origin: Square, board: Board):
        """
        Return the available squares from origin for a bishop.
        A bishop moves in diagonal, and can't go threw another piece,
        Can take a piece with different color
        @return: list of reachable squares
        """
        available_squares: list[Square] = []
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
        @return: 1001 or 0001
        """
        return 0b1001 if self.color == Color.WHITE else 0b0001

    def __repr__(self):
        return "B" if self.color == Color.WHITE else "b"
