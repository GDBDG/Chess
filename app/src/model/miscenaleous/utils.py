"""
Some useful functions
"""
from app.src.exceptions.missing_king_error import MissingKingError
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.piece_type import PieceType


def is_king_in_check(square_list, piece_list, color) -> bool:
    """
    Return a boolean saying if the king pf color <color> is in check
    Raise an error if there is no king
    :param square_list: {(column, row): Square} dict of the squares in the game
    :param piece_list: {(Column, row): Piece} dict of the pieces in the game
    :param color: color of the king
    :return: boolean : is the is_king_in_check in check
    """
    try:
        king = get_king(piece_list, color)
    except MissingKingError as error:
        raise error
    else:
        return king.is_in_check(square_list, piece_list)


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
