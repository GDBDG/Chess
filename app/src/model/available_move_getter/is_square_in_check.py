"""
Utils function to know if a square is in check
"""
from app.src.model.available_move_getter.available_moves import get_available_moves
from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


def is_square_in_check(
    color: Color, square: Square, piece_dict: dict[Square, Piece]
) -> bool:
    """
    Return a boolean indicating if a piece in a different color can move
    to square (indicates if a piece of color *color* is in check)
    @param color: color of the piece that we check if it can be taken
    @param square: the square where we check if it can be taken
    @param piece_dict:  dict of the pieces in the game
    @return: boolean
    """
    return any(
        piece.color != color
        and square
        in list(map(lambda x: x.destination, get_available_moves(origin, piece_dict)))
        for origin, piece in piece_dict.items()
    )
