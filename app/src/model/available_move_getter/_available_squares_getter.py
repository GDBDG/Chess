"""
Auxiliaries function for available_moves
"""
from copy import copy

from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.utils import _get_current_color
from app.src.model.pieces.piece import Piece


def _available_squares_bishop(
    origin: Square, piece_dict: dict[Square, Piece]
) -> [Square]:
    """
    A bishop moves in diagonal, and can't go threw another piece,
    Can take a piece with different color
    @return: list of reachable squares
    """
    available_squares: list[Square] = []
    # diagonal right up squares
    available_squares.extend(
        _available_squares_diagonal_right_up(
            origin,
            piece_dict,
        )
    )
    # diagonal right down squares
    available_squares.extend(
        _available_squares_diagonal_right_down(
            origin,
            piece_dict,
        )
    )
    # diagonal left up squares
    available_squares.extend(
        _available_squares_diagonal_left_up(
            origin,
            piece_dict,
        )
    )
    # diagonal left down squares
    available_squares.extend(
        _available_squares_diagonal_left_down(
            origin,
            piece_dict,
        )
    )
    return available_squares


def _available_squares_diagonal_left_down(
    origin: Square,
    piece_dict: dict[Square, Piece],
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
        piece_dict,
    )


def _available_squares_diagonal_left_up(
    origin: Square,
    piece_dict: dict[Square, Piece],
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
        piece_dict,
    )


def _available_squares_diagonal_right_down(
    origin: Square,
    piece_dict: dict[Square, Piece],
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
        piece_dict,
    )


def _available_squares_diagonal_right_up(
    origin: Square,
    piece_dict: dict[Square, Piece],
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
        piece_dict,
    )


def _available_squares_below(
    origin: Square,
    piece_dict: dict[Square, Piece],
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
        piece_dict,
    )


def _available_squares_upper(
    origin: Square,
    piece_dict: dict[Square, Piece],
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
        piece_dict,
    )


def _available_squares_on_left(
    origin: Square,
    piece_dict: dict[Square, Piece],
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
        piece_dict,
    )


def _available_squares_on_right(
    origin: Square,
    piece_dict: dict[Square, Piece],
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
        piece_dict,
    )


def _available_square_on_side_line(
    origin: Square,
    squares: [Square],
    piece_dict: dict[Square, Piece],
):
    """
    Returns the available squares on only one side.
    (for ex on the right side, or diagonal right).
    (iterate on a square list)
    @params squares:
    @param piece_dict: a list of pieces (represents the pieces in the game)
    @return: square_list of available squares designated by the product of columns and rows
    """
    color = _get_current_color(origin, piece_dict)
    available_squares = []
    for square in squares:
        # if there is a piece on the square
        if square in piece_dict:
            # if the piece can take the other piece
            if piece_dict[square].color != color:
                available_squares.append(square)
            break
        # if there is no piece on the square
        available_squares.append(square)
    return available_squares


def _available_squares_knight(
    origin: Square, piece_dict: dict[Square, Piece]
) -> [Square]:
    """
    Return the available squares
    @return: list of reachable squares
    """
    available_squares: list[Square] = []
    color = _get_current_color(origin, piece_dict)
    # up squares
    _add_square(
        origin.column.value - 1,
        origin.row + 2,
        available_squares,
    )
    _add_square(
        origin.column.value + 1,
        origin.row + 2,
        available_squares,
    )
    # down squares
    _add_square(
        origin.column.value - 1,
        origin.row - 2,
        available_squares,
    )
    _add_square(
        origin.column.value + 1,
        origin.row - 2,
        available_squares,
    )
    # right squares
    _add_square(
        origin.column.value + 2,
        origin.row - 1,
        available_squares,
    )
    _add_square(
        origin.column.value + 2,
        origin.row + 1,
        available_squares,
    )
    # left squares
    _add_square(
        origin.column.value - 2,
        origin.row - 1,
        available_squares,
    )
    _add_square(
        origin.column.value - 2,
        origin.row + 1,
        available_squares,
    )
    # Remove squares in available_squares if there is a piece with the same color
    for square in copy(available_squares):
        if square in piece_dict and piece_dict[square].color == color:
            available_squares.remove(square)
    return available_squares


def _add_square(column: int, row: int, available_squares: [Square]):
    """
    Add the square with coordinate column and row in available_squares
    if it is in square_list
    @param row: row coordinate int value
    @param column: column coordinate (int value)
    @param available_squares: a list of square where the square will be added
    """
    if 1 <= column <= 8 and 1 <= row <= 8:
        available_squares.append(Square(Column(column), row))


def _step_next_move(origin: Square, piece_dict: dict[Square, Piece]) -> int:
    """
    Return +1 if the piece in origin is white, -1 if the piece is black
    else raises a ValueError
    @param origin: origin Square for the move
    @param piece_dict: dict with the pieces in the game
    @return: the step for the pawn move (+1 or -1)
    """
    color = piece_dict[origin].color
    return int(color == Color.WHITE) - int(color == Color.BLACK)


def _available_squares_queen(
    origin: Square, piece_dict: dict[Square, Piece]
) -> [Square]:
    """
    A queen move in line and diagonal, and can't go threw another piece,
    but can take a piece with a different color.
    @return: list of reachable squares
    """
    available_squares: list[Square] = []
    # right squares
    available_squares.extend(
        _available_squares_on_right(
            origin,
            piece_dict,
        )
    )
    # left squares
    available_squares.extend(
        _available_squares_on_left(
            origin,
            piece_dict,
        )
    )
    # up squares
    available_squares.extend(
        _available_squares_upper(
            origin,
            piece_dict,
        )
    )
    # down squares
    available_squares.extend(
        _available_squares_below(
            origin,
            piece_dict,
        )
    )
    # diagonal right up squares
    available_squares.extend(
        _available_squares_diagonal_right_up(
            origin,
            piece_dict,
        )
    )
    # diagonal right down squares
    available_squares.extend(
        _available_squares_diagonal_right_down(
            origin,
            piece_dict,
        )
    )
    # diagonal left up squares
    available_squares.extend(
        _available_squares_diagonal_left_up(
            origin,
            piece_dict,
        )
    )
    # diagonal left down squares
    available_squares.extend(
        _available_squares_diagonal_left_down(
            origin,
            piece_dict,
        )
    )
    return available_squares


def _available_squares_rook(
    origin: Square, piece_dict: dict[Square, Piece]
) -> [Square]:
    """
    A rook move in line, and can't go threw another piece,
    but can take a piece with a different color.
    @param piece_dict: {(Column, row): Piece} dict of the pieces in the game
    @return: list of reachable squares
    """
    available_squares: list[Square] = []
    # right squares
    available_squares.extend(
        _available_squares_on_right(
            origin,
            piece_dict,
        )
    )
    # left squares
    available_squares.extend(
        _available_squares_on_left(
            origin,
            piece_dict,
        )
    )
    # up squares
    available_squares.extend(
        _available_squares_upper(
            origin,
            piece_dict,
        )
    )
    # down squares
    available_squares.extend(
        _available_squares_below(
            origin,
            piece_dict,
        )
    )
    return available_squares
