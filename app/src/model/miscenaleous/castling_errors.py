"""
Error messages for castling
"""
from enum import Enum


class CastlingErrors(Enum):
    """
    Enumerate, key : int between 1 and 4, value : message
    """

    ROOK_HAS_MOVED = "The rook has moved"
    KING_HAS_MOVED = "The king has moved"
    KING_IN_CHECK = "The king is in check"
    NOT_EMPTY_PATH = "There is a piece in the castling path"
    PATH_IN_CHECK = "The king is in check during the movement"
    VALID = "Castling valid"
