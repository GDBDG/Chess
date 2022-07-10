"""
Implementation of the king
Check if the king is in check
Castling :
"""
from copy import copy

from app.src.back.chess_board.square import Square
from app.src.back.pieces.piece import Piece


class King(Piece):
    """
    Implementation of king
    """

    def available_squares(self, square_list, piece_list) -> [Square]:
        """
        A king can move like a queen, but only of one square
        Can't be in check (makes the verification)
        :param square_list: list of available squares
        :param piece_list: list of others pieces in the game
        :return: list of reachable squares
        """
        available_squares: list[Square] = []
        # Add the squares
        Piece._add_square(
            self.column.value - 1,
            self.row - 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value - 1,
            self.row,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value - 1,
            self.row + 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value,
            self.row - 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value,
            self.row + 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value + 1,
            self.row - 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value + 1,
            self.row,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value + 1,
            self.row + 1,
            square_list,
            available_squares,
        )
        # Remove the squares if the king is in check
        # Remove the squares if there is a piece on the same color
        for square in copy(available_squares):
            if Piece.is_in_check(self.color, square, square_list, piece_list,) or (
                (square.column, square.row) in piece_list
                and piece_list[square.column, square.row].color == self.color
            ):
                available_squares.remove(square)

        return available_squares
