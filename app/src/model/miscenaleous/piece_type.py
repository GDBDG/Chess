"""
Enum for the type of pieces in the game
"""
from enum import Enum


class PieceType(Enum):
    """
    Enum class for the piece
    """

    BISHOP = "bishop"
    KING = "King"
    KNIGHT = "knight"
    PAWN = "pawn"
    PIECE = "piece"
    QUEEN = "queen"
    ROOK = "rook"
