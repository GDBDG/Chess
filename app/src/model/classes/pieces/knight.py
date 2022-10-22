"""
Knight
"""
from copy import copy

from app.src.model.classes.pieces.piece import Piece
from app.src.model.classes.square import Square
from app.src.model.events.moves.knight_move import KnightMove
from app.src.model.game.board import Board
from app.src.model.miscenaleous.color import Color


class Knight(Piece):
    """
    Knight classes
    """
    move = KnightMove

    def available_squares(self, origin: Square, board: Board):
        available_squares: list[Square] = []
        color = board.get_current_color(origin)
        # up squares
        Square.add_square(
            origin.column.value - 1,
            origin.row + 2,
            available_squares,
        )
        Square.add_square(
            origin.column.value + 1,
            origin.row + 2,
            available_squares,
        )
        # down squares
        Square.add_square(
            origin.column.value - 1,
            origin.row - 2,
            available_squares,
        )
        Square.add_square(
            origin.column.value + 1,
            origin.row - 2,
            available_squares,
        )
        # right squares
        Square.add_square(
            origin.column.value + 2,
            origin.row - 1,
            available_squares,
        )
        Square.add_square(
            origin.column.value + 2,
            origin.row + 1,
            available_squares,
        )
        # left squares
        Square.add_square(
            origin.column.value - 2,
            origin.row - 1,
            available_squares,
        )
        Square.add_square(
            origin.column.value - 2,
            origin.row + 1,
            available_squares,
        )
        # Remove squares in available_squares if there is a piece with the same color
        for square in copy(available_squares):
            if square in board.piece_dict and board.piece_dict[square].color == color:
                available_squares.remove(square)
        return available_squares

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1011 or 0011
        """
        return 0b1011 if self.color == Color.WHITE else 0b0011

    def __repr__(self):
        return "KN" if self.color == Color.WHITE else "kn"
