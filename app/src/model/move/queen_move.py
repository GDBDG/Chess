"""
Queen move
"""
from app.src.logger import LOGGER
from app.src.model.game.square import Square
from app.src.model.move.move import Move
from app.src.model.pieces.piece import Piece


class QueenMove(Move):
    """
    Queeen moves
    """

    @staticmethod
    def get_available_moves(origin: Square, piece_dict: dict[Square, Piece]):
        LOGGER.info("Getting available moves called for queen")
        return [
            QueenMove(origin, destination)
            for destination in QueenMove._available_squares(origin, piece_dict)
        ]

    @staticmethod
    def _available_squares(origin: Square, piece_dict: dict[Square, Piece]) -> [Square]:
        """
        A queen move in line and diagonal, and can't go threw another piece,
        but can take a piece with a different color.
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
        # diagonal right up squares
        available_squares.extend(
            Move._available_squares_diagonal_right_up(
                origin,
                piece_dict,
            )
        )
        # diagonal right down squares
        available_squares.extend(
            Move._available_squares_diagonal_right_down(
                origin,
                piece_dict,
            )
        )
        # diagonal left up squares
        available_squares.extend(
            Move._available_squares_diagonal_left_up(
                origin,
                piece_dict,
            )
        )
        # diagonal left down squares
        available_squares.extend(
            Move._available_squares_diagonal_left_down(
                origin,
                piece_dict,
            )
        )
        return available_squares
