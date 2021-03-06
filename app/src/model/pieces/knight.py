"""
Knight
Movements : moves 2 squares in one direction, then one in the other
"""
from copy import copy

from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.pieces.piece import Piece


class Knight(Piece):
    """
    Knight class
    """

    piece_type = PieceType.KNIGHT

    def available_squares(self, square_list, piece_list) -> [Square]:
        """
        Return the available squares
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: list of reachable squares
        """
        available_squares = []
        # up squares
        Piece._add_square(
            self.column.value - 1,
            self.row + 2,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value + 1,
            self.row + 2,
            square_list,
            available_squares,
        )
        # down squares
        Piece._add_square(
            self.column.value - 1,
            self.row - 2,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value + 1,
            self.row - 2,
            square_list,
            available_squares,
        )
        # right squares
        Piece._add_square(
            self.column.value + 2,
            self.row - 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value + 2,
            self.row + 1,
            square_list,
            available_squares,
        )
        # left squares
        Piece._add_square(
            self.column.value - 2,
            self.row - 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value - 2,
            self.row + 1,
            square_list,
            available_squares,
        )
        # Remove squares in available_squares if there is a piece with the same color
        for square in copy(available_squares):
            if (square.column, square.row) in piece_list and piece_list[
                (square.column, square.row)
            ].color == self.color:
                available_squares.remove(square)
        return available_squares
