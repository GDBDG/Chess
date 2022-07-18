"""
Some useful functions
"""
from app.src.exceptions.missing_king_error import MissingKingError
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.piece_type import PieceType


def get_king(piece_list, color: Color):
    """
    Return the King with the color <color> in the piece_list
    Raises an error if there is no King
    :param piece_list: {(Column, row): Piece} dict of the pieces in the game
    :param color: color of the king
    :return: the instance of the king
    """
    king = next(
        (
            piece
            for piece in piece_list.values()
            if piece.piece_type == PieceType.KING and piece.color == color
        ),
        None,
    )
    if king is None:
        raise MissingKingError
    return king
