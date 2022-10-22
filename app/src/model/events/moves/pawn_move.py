"""
Forward moves (one square, no capture
"""
from app.src.model.events.moves.move import Move
from app.src.model.game.board import Board
from app.src.model.game.square import Square


class PawnMove(Move):
    """
    Pawn moves (one square, no capture)
    """

    def available_squares(self, origin: Square, board: Board):
        pass
