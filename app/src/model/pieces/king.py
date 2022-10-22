"""
King
"""
from copy import copy

from app.src.model.events.moves.king_move import KingMove
from app.src.model.game.board import Board
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class King(Piece):
    """
    King class
    """
    move = KingMove

    @staticmethod
    def available_squares(origin: Square, board: Board):
        """
       The king moves exactly one square horizontally, vertically, or diagonally
       (Does not return the castling squares
       @param origin:
       @param board:
       @return:
           """
        available_squares = []
        color = board.piece_dict[origin].color
        Square.add_square(
            origin.column.value - 1,
            origin.row - 1,
            available_squares,
        )
        Square.add_square(origin.column.value - 1, origin.row, available_squares)
        Square.add_square(origin.column.value - 1, origin.row + 1, available_squares)
        Square.add_square(origin.column.value, origin.row - 1, available_squares)
        Square.add_square(origin.column.value, origin.row + 1, available_squares)
        Square.add_square(origin.column.value + 1, origin.row - 1, available_squares)
        Square.add_square(origin.column.value + 1, origin.row, available_squares)
        Square.add_square(origin.column.value + 1, origin.row + 1, available_squares)
        for square in copy(available_squares):
            if square in board.piece_dict and board.piece_dict[square].color == color:
                available_squares.remove(square)
        return available_squares

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1010 or 0010
        """
        return 0b1010 if self.color == Color.WHITE else 0b0010

    def __repr__(self):
        return "K" if self.color == Color.WHITE else "k"
