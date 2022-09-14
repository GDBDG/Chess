"""
Knight Promotion.
Promotion: when a pawn reaches the last line: can turn into another piece.
Simplification: only Knight and knight (bishop and rook are useless)
"""
from app.src.model.game.square import Square
from app.src.model.move.pawn_move import PawnMove
from app.src.model.pieces.knight import Knight
from app.src.model.pieces.piece import Piece


class KnightPromotion(PawnMove):
    """
    Knight promotion class.
    """

    def __repr__(self):
        return (
            f"{self.origin.column.name}{self.origin.row}"
            f"{self.destination.column.name}{self.destination.row}"
            f"=K"
        )

    def apply_move(self, piece_dict: dict[Square, Piece]) -> bool:
        """
        Replace the pawn by a knight
        @param piece_dict: pieces in the game
        @return: false : no capture
        """
        piece_dict[self.destination] = Knight(piece_dict[self.origin].color)
        piece_dict.pop(self.origin)
        return False
