"""
Some useful functions
"""
from app.src.exceptions.missing_king_error import MissingKingError
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.king import King
from app.src.model.pieces.piece import Piece


def get_king(piece_dict: dict[Square, Piece], color: Color) -> Square:
    """
    Return the King with the color <color> in the piece_list
    Raises an error if there is no King
    @param piece_dict: {(Column, row): Piece} dict of the pieces in the game
    @param color: color of the king
    @return: the origin of the king
    """
    king = next(
        (
            square
            for square in piece_dict
            if type(piece_dict[square]) == King and piece_dict[square].color == color
        ),
        None,
    )
    if king is None:
        raise MissingKingError
    return king


def _get_current_color(
    origin: Square,
    piece_dict: dict[Square, Piece],
) -> Color:
    """
    Get the color of the current player, with the piece list and the coordinates
    @return:
    """
    return piece_dict[origin].color
