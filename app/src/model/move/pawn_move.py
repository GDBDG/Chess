"""
Forward move (one square, no capture
"""
from app.src.model.game.square import Square
from app.src.model.move.move import Move
from app.src.model.pieces.piece import Piece


class PawnMove(Move):
    @staticmethod
    def get_available_moves(origin: Square, piece_dict: dict[Square, Piece],):
        pass
