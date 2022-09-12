"""
Knight Promotion.
Promotion: when a pawn reaches the last line: can turn into another piece.
Simplification: only Knight and knight (bishop and rook are useless)
"""
from app.src.model.move.pawn_move import PawnMove


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
