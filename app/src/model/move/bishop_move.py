"""
Moves for the bishop
"""
from app.src.logger import LOGGER
from app.src.model.game.square import Square
from app.src.model.move.move import Move
from app.src.model.pieces.piece import Piece


class BishopMove(Move):
    """
    Bishop moves
    """

    @staticmethod
    def get_available_moves(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        LOGGER.info("Get available moves called for bishop")
        return [
            BishopMove(origin, destination)
            for destination in BishopMove._available_squares(origin, piece_dict)
        ]

    @staticmethod
    def _available_squares(origin: Square, piece_dict: dict[Square, Piece]) -> [Square]:
        """
        A bishop moves in diagonal, and can't go threw another piece,
        Can take a piece with different color
        @return: list of reachable squares
        """
        available_squares: list[Square] = []
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
