"""
Square getter for queen
"""
from app.src.model.available_move_getter.available_squares_getter import (
    available_squares_on_right,
    available_squares_on_left,
    available_squares_upper,
    available_squares_below,
    available_squares_diagonal_right_up,
    available_squares_diagonal_right_down,
    available_squares_diagonal_left_up,
    available_squares_diagonal_left_down,
)
from app.src.model.classes.square import Square
from app.src.model.states.board import Board


def queen_available_squares(origin: Square, board: Board) -> [Square]:
    """
    A queen moves in line and diagonal, and can't go threw another piece,
    but can take a piece with a different color.
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
    # diagonal right up squares
    available_squares_list.extend(available_squares_diagonal_right_up(origin, board))
    # diagonal right down squares
    available_squares_list.extend(available_squares_diagonal_right_down(origin, board))
    # diagonal left up squares
    available_squares_list.extend(available_squares_diagonal_left_up(origin, board))
    # diagonal left down squares
    available_squares_list.extend(available_squares_diagonal_left_down(origin, board))
    return available_squares_list
