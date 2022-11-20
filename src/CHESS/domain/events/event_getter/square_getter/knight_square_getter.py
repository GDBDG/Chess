"""
Square getter for knight, from origin
"""
from copy import copy

from src.CHESS.domain.classes.square import Square
from src.CHESS.domain.states.board import Board


def knight_available_squares(origin: Square, board: Board) -> [Square]:
    """
    Return tha available squares for a knight.
    A knight moves to one of the nearest squares not on the same rank, file, or diagonal.
    (This can be thought of as moving two squares horizontally then one square vertically,
    or moving one square horizontally then two squares vertically—i.e. in an "L" pattern.)
    The knight is not blocked by other pieces; it jumps to the new location.
    @param origin:
    @param board:
    @return:
    """
    available_squares_list: list[Square] = []
    color = board.get_current_color(origin)
    # up squares
    Square.add_square(
        origin.column.value - 1,
        origin.row + 2,
        available_squares_list,
    )
    Square.add_square(
        origin.column.value + 1,
        origin.row + 2,
        available_squares_list,
    )
    # down squares
    Square.add_square(
        origin.column.value - 1,
        origin.row - 2,
        available_squares_list,
    )
    Square.add_square(
        origin.column.value + 1,
        origin.row - 2,
        available_squares_list,
    )
    # right squares
    Square.add_square(
        origin.column.value + 2,
        origin.row - 1,
        available_squares_list,
    )
    Square.add_square(
        origin.column.value + 2,
        origin.row + 1,
        available_squares_list,
    )
    # left squares
    Square.add_square(
        origin.column.value - 2,
        origin.row - 1,
        available_squares_list,
    )
    Square.add_square(
        origin.column.value - 2,
        origin.row + 1,
        available_squares_list,
    )
    # Remove squares in available_squares if there is a piece with the same color
    for square in copy(available_squares_list):
        if square in board.piece_dict and board.piece_dict[square].color == color:
            available_squares_list.remove(square)
    return available_squares_list
