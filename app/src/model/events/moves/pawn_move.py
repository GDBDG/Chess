"""
Forward moves (one square, no capture
"""
from app.src.model.classes.square import Square
from app.src.model.events.moves.move import Move
from app.src.model.game.board import Board


class PawnMove(Move):
    """
    Pawn moves (one square, no capture)
    """

    def available_squares(self, origin: Square, board: Board):
        pass
