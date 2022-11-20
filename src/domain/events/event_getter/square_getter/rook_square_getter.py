"""
Rook square getter, form, origin@
"""
from src.domain.classes.square import Square
from src.domain.events.event_getter.square_getter.utils_available_squares_getter import (
    available_squares_on_right,
    available_squares_on_left,
    available_squares_upper,
    available_squares_below,
)
from src.domain.states.board import Board


def rook_available_squares(origin: Square, board: Board) -> [Square]:
    """
    A rook moves in line, and can't go threw another piece,
    but can take a piece with a different color.
    @param origin:
    @param board:
    @return: list of reachable squares
    """
    available_squares_list: list[Square] = []
    # right squares
    available_squares_list.extend(available_squares_on_right(origin, board))
    # left squares
    available_squares_list.extend(available_squares_on_left(origin, board))
    # up squares
    available_squares_list.extend(available_squares_upper(origin, board))
    # down squares
    available_squares_list.extend(available_squares_below(origin, board))
    return available_squares_list
