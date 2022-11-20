"""
Square getter for king, form origin
"""
from copy import copy

from src.domain.classes.square import Square
from src.domain.states.board import Board


def king_available_squares(origin: Square, board: Board):
    """
    The king moves exactly one square horizontally, vertically, or diagonally
    (Does not return the castling squares
    @param origin:
    @param board:
    @return:
    """
    available_squares_list = []
    color = board.piece_dict[origin].color
    Square.add_square(
        origin.column.value - 1,
        origin.row - 1,
        available_squares_list,
    )
    Square.add_square(origin.column.value - 1, origin.row, available_squares_list)
    Square.add_square(origin.column.value - 1, origin.row + 1, available_squares_list)
    Square.add_square(origin.column.value, origin.row - 1, available_squares_list)
    Square.add_square(origin.column.value, origin.row + 1, available_squares_list)
    Square.add_square(origin.column.value + 1, origin.row - 1, available_squares_list)
    Square.add_square(origin.column.value + 1, origin.row, available_squares_list)
    Square.add_square(origin.column.value + 1, origin.row + 1, available_squares_list)
    for square in copy(available_squares_list):
        if square in board.piece_dict and board.piece_dict[square].color == color:
            available_squares_list.remove(square)
    return available_squares_list
