"""
Square getter for all pieces except pawn
For the king, it does not return the castling squares
"""
from src.domain.classes.pieces.bishop import Bishop
from src.domain.classes.pieces.king import King
from src.domain.classes.pieces.knight import Knight
from src.domain.classes.pieces.queen import Queen
from src.domain.classes.pieces.rook import Rook
from src.domain.classes.square import Square
from src.domain.events.event_getter.square_getter.bishop_square_getter import (
    bishop_available_squares,
)
from src.domain.events.event_getter.square_getter.king_square_getter import (
    king_available_squares,
)
from src.domain.events.event_getter.square_getter.knight_square_getter import (
    knight_available_squares,
)
from src.domain.events.event_getter.square_getter.queen_square_getter import (
    queen_available_squares,
)
from src.domain.events.event_getter.square_getter.rook_square_getter import (
    rook_available_squares,
)
from src.domain.states.board import Board
from src.logger import LOGGER


def available_squares(origin: Square, board: Board) -> [Square]:
    """
    Return the squares available for a piece, except pawn.
    It should be used only in square_available_moves_no_castling.
    @param origin:
    @param board:
    @return:
    """
    try:
        origin_piece = board.piece_dict[origin]
    except KeyError as error:
        LOGGER.error("available square called from origin with no square")
        raise error
    if isinstance(origin_piece, Bishop):
        return bishop_available_squares(origin, board)
    if isinstance(origin_piece, King):
        return king_available_squares(origin, board)
    if isinstance(origin_piece, Knight):
        return knight_available_squares(origin, board)
    if isinstance(origin_piece, Queen):
        return queen_available_squares(origin, board)
    if isinstance(origin_piece, Rook):
        return rook_available_squares(origin, board)
    raise ValueError(
        "origin piece does not match an available type for available_squares"
    )
