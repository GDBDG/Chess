"""
Forward move (one square, no capture
"""

from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.move.move import Move
from app.src.model.pieces.piece import Piece


class PawnMove(Move):
    """
    Pawn move (one square, no capture)
    """

    @staticmethod
    def get_available_moves(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        available_moves = []
        if Square(origin.column, origin.row + PawnMove._step_next_move(origin, piece_dict)) not in piece_dict:
            available_moves.append(
                PawnMove(origin, Square(origin.column, origin.row + PawnMove._step_next_move(origin, piece_dict))))
        return available_moves

    @staticmethod
    def _step_next_move(origin: Square, piece_dict: dict[Square, Piece]) -> int:
        """
        Return +1 if the piece in origin is white, -1 if the piece is black
        else raises a ValueError
        @param origin: origin Square for the move
        @param piece_dict: dict with the pieces in the game
        @return: the step for the pawn move (+1 or -1)
        """
        color = piece_dict[origin].color
        return int(color == Color.WHITE) - int(color == Color.BLACK)
