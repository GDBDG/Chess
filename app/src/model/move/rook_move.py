"""
Moves for the rook
"""
from app.src.logger import LOGGER
from app.src.model.game.square import Square
from app.src.model.move.move import Move
from app.src.model.pieces.piece import Piece


class RookMove(Move):
    """
    Rook moves
    """

    @staticmethod
    def get_available_moves(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        LOGGER.info("Get available moves called for rook")
        return [
            RookMove(origin, destination)
            for destination in RookMove._available_squares(origin, piece_dict)
        ]

    @staticmethod
    def _available_squares(origin: Square, piece_dict: dict[Square, Piece]) -> [Square]:
        """
        A rook move in line, and can't go threw another piece,
        but can take a piece with a different color.
        @param piece_dict: {(Column, row): Piece} dict of the pieces in the game
        @return: list of reachable squares
        """
        available_squares: list[Square] = []
        # right squares
        available_squares.extend(
            Move._available_squares_on_right(
                origin,
                piece_dict,
            )
        )
        # left squares
        available_squares.extend(
            Move._available_squares_on_left(
                origin,
                piece_dict,
            )
        )
        # up squares
        available_squares.extend(
            Move._available_squares_upper(
                origin,
                piece_dict,
            )
        )
        # down squares
        available_squares.extend(
            Move._available_squares_below(
                origin,
                piece_dict,
            )
        )
        return available_squares
