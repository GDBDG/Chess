"""
Auxiliaries function for available_moves
"""

from src.CHESS.domain.classes.const.color import Color
from src.CHESS.domain.classes.const.column import Column
from src.CHESS.domain.classes.square import Square
from src.CHESS.domain.states.board import Board


def available_squares_diagonal_left_down(
    origin: Square,
    board: Board,
):
    """
    Returns the available squares on the right on the piece
    @return:
    """
    return _available_square_on_side_line(
        origin,
        [
            Square(column, row)
            for column, row in zip(
            map(Column, range(origin.column.value - 1, 0, -1)),
            range(origin.row - 1, 0, -1),
        )
        ],
        board,
    )


def available_squares_diagonal_left_up(
    origin: Square,
    board: Board,
):
    """
    Returns the available squares on the right on the piece
    @return:
    """
    return _available_square_on_side_line(
        origin,
        [
            Square(column, row)
            for column, row in zip(
            map(Column, range(origin.column.value - 1, 0, -1)),
            range(origin.row + 1, 9),
        )
        ],
        board,
    )


def available_squares_diagonal_right_down(
    origin: Square,
    board: Board,
):
    """
    Returns the available squares on the right on the piece
    @return:
    """
    return _available_square_on_side_line(
        origin,
        [
            Square(column, row)
            for column, row in zip(
            map(Column, range(origin.column.value + 1, 9)),
            range(origin.row - 1, 0, -1),
        )
        ],
        board,
    )


def available_squares_diagonal_right_up(
    origin: Square,
    board: Board,
):
    """
    Returns the available squares on the right on the piece
    @return:
    """
    return _available_square_on_side_line(
        origin,
        [
            Square(column, row)
            for column, row in zip(
            map(Column, range(origin.column.value + 1, 9)),
            range(origin.row + 1, 9),
        )
        ],
        board,
    )


def available_squares_below(
    origin: Square,
    board: Board,
):
    """
    Returns the available squares on the right on the piece
    @return:
    """
    return _available_square_on_side_line(
        origin,
        [
            Square(column, row)
            for column, row in zip(
            [origin.column] * (origin.row - 1),
            range(origin.row - 1, 0, -1),
        )
        ],
        board,
    )


def available_squares_upper(
    origin: Square,
    board: Board,
):
    """
    Returns the available squares on the right on the piece
    @return:
    """
    return _available_square_on_side_line(
        origin,
        [
            Square(column, row)
            for column, row in zip(
            [origin.column] * (8 - origin.row),
            range(origin.row + 1, 9),
        )
        ],
        board,
    )


def available_squares_on_left(
    origin: Square,
    board: Board,
):
    """
    Returns the available squares on the right on the piece

    """
    return _available_square_on_side_line(
        origin,
        [
            Square(column, row)
            for column, row in zip(
            map(
                Column,
                range(origin.column.value - 1, 0, -1),
            ),
            [origin.row] * (origin.column.value - 1),
        )
        ],
        board,
    )


def available_squares_on_right(
    origin: Square,
    board: Board,
):
    """
    Returns the available squares on the right on the piece
    @param piece_dict: {(Column, row): Piece} dict of the pieces in the game
    @return:
    """
    return _available_square_on_side_line(
        origin,
        [
            Square(column, row)
            for column, row in zip(
            map(
                Column,
                range(origin.column.value + 1, 9),
            ),
            [origin.row] * (8 - origin.column.value),
        )
        ],
        board,
    )


def _available_square_on_side_line(origin: Square, squares: [Square], board: Board):
    """
    Returns the available squares on only one side.
    (for ex on the right side, or diagonal right).
    (iterate on a square list)
    @params squares:
    @param piece_dict: a list of pieces (represents the pieces in the game)
    @return: square_list of available squares designated by the product of columns and rows
    """
    color = board.get_current_color(origin)
    available_squares = []
    for square in squares:
        # if there is a piece on the square
        if square in board.piece_dict:
            # if the piece can take the other piece
            if board.piece_dict[square].color != color:
                available_squares.append(square)
            break
        # if there is no piece on the square
        available_squares.append(square)
    return available_squares


def step_next_move(origin: Square, piece_dict) -> int:
    """
    Return +1 if the piece in origin is white, -1 if the piece is black
    else raises a ValueError
    @param origin: origin Square for the moves
    @param piece_dict: dict with the pieces in the game
    @return: the step for the pawn moves (+1 or -1)
    """
    color = piece_dict[origin].color
    return int(color == Color.WHITE) - int(color == Color.BLACK)
