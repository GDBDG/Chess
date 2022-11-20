"""
Square getter for a bishop (available square from origin}
"""
from src.domain.classes.square import Square
from src.domain.events.event_getter.square_getter.utils_available_squares_getter import (
    available_squares_diagonal_right_up,
    available_squares_diagonal_right_down,
    available_squares_diagonal_left_up,
    available_squares_diagonal_left_down,
)
from src.domain.states.board import Board


def bishop_available_squares(origin: Square, board: Board):
    """
    Return the available squares from origin for a bishop.
    A bishop moves in diagonal, and can't go throw another piece,
    Can take a piece with different color
    @return: list of reachable squares
    """
    available_squares_list: list[Square] = []
    # diagonal right up squares
    available_squares_list.extend(available_squares_diagonal_right_up(origin, board))
    # diagonal right down squares
    available_squares_list.extend(available_squares_diagonal_right_down(origin, board))
    # diagonal left up squares
    available_squares_list.extend(available_squares_diagonal_left_up(origin, board))
    # diagonal left down squares
    available_squares_list.extend(available_squares_diagonal_left_down(origin, board))
    return available_squares_list
