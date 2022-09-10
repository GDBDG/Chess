"""
Moves for the knight
"""
from copy import copy

from app.src.logger import LOGGER
from app.src.model.game.square import Square
from app.src.model.miscenaleous.column import Column
from app.src.model.move.move import Move
from app.src.model.pieces.piece import Piece


class KnightMove(Move):
    """
    Knight move
    """

    @staticmethod
    def get_available_moves(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        LOGGER.info("Get available moves for knight")
        return [
            KnightMove(origin, destination)
            for destination in KnightMove._available_squares(origin, piece_dict)
        ]

    @staticmethod
    def _add_square(column: int, row: int, available_squares: [Square]):
        """
        Add the square with coordinate column and row in available_squares
        if it is in square_list
        @param row: row coordinate int value
        @param column: column coordinate (int value)
        @param available_squares: a list of square where the square will be added
        """
        if 1 <= column <= 8 and 1 <= row <= 8:
            available_squares.append(Square(Column(column), row))

    @staticmethod
    def _available_squares(origin: Square, piece_dict: dict[Square, Piece]) -> [Square]:
        """
        Return the available squares
        @return: list of reachable squares
        """
        available_squares: list[Square] = []
        color = Move._get_current_color(origin, piece_dict)
        # up squares
        KnightMove._add_square(
            origin.column.value - 1,
            origin.row + 2,
            available_squares,
        )
        KnightMove._add_square(
            origin.column.value + 1,
            origin.row + 2,
            available_squares,
        )
        # down squares
        KnightMove._add_square(
            origin.column.value - 1,
            origin.row - 2,
            available_squares,
        )
        KnightMove._add_square(
            origin.column.value + 1,
            origin.row - 2,
            available_squares,
        )
        # right squares
        KnightMove._add_square(
            origin.column.value + 2,
            origin.row - 1,
            available_squares,
        )
        KnightMove._add_square(
            origin.column.value + 2,
            origin.row + 1,
            available_squares,
        )
        # left squares
        KnightMove._add_square(
            origin.column.value - 2,
            origin.row - 1,
            available_squares,
        )
        KnightMove._add_square(
            origin.column.value - 2,
            origin.row + 1,
            available_squares,
        )
        # Remove squares in available_squares if there is a piece with the same color
        for square in copy(available_squares):
            if square in piece_dict and piece_dict[square].color == color:
                available_squares.remove(square)
        return available_squares
