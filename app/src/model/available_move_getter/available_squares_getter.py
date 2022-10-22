"""
Auxiliaries function for available_moves
"""
from copy import copy

from app.src.model.classes.const.color import Color
from app.src.model.classes.const.column import Column
from app.src.model.classes.square import Square
from app.src.model.states.board import Board


def available_squares_bishop(origin: Square, piece_dict) -> [Square]:
    """
    A bishop moves in diagonal, and can't go threw another piece,
    Can take a piece with different color
    @return: list of reachable squares
    """
    available_squares: list[Square] = []
    # diagonal right up squares
    available_squares.extend(
        available_squares_diagonal_right_up(
            origin,
            piece_dict,
        )
    )
    # diagonal right down squares
    available_squares.extend(
        available_squares_diagonal_right_down(
            origin,
            piece_dict,
        )
    )
    # diagonal left up squares
    available_squares.extend(
        available_squares_diagonal_left_up(
            origin,
            piece_dict,
        )
    )
    # diagonal left down squares
    available_squares.extend(
        available_squares_diagonal_left_down(
            origin,
            piece_dict,
        )
    )
    return available_squares


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


def available_squares_king(origin: Square, piece_dict) -> [Square]:
    """
    The king moves exactly one square horizontally, vertically, or diagonally
    (Does not return the castling squares
    @param origin:
    @param piece_dict:
    @return:
    """
    available_squares = []
    color = piece_dict[origin].color
    Square.add_square(
        origin.column.value - 1,
        origin.row - 1,
        available_squares,
    )
    Square.add_square(origin.column.value - 1, origin.row, available_squares)
    Square.add_square(origin.column.value - 1, origin.row + 1, available_squares)
    Square.add_square(origin.column.value, origin.row - 1, available_squares)
    Square.add_square(origin.column.value, origin.row + 1, available_squares)
    Square.add_square(origin.column.value + 1, origin.row - 1, available_squares)
    Square.add_square(origin.column.value + 1, origin.row, available_squares)
    Square.add_square(origin.column.value + 1, origin.row + 1, available_squares)
    for square in copy(available_squares):
        if square in piece_dict and piece_dict[square].color == color:
            available_squares.remove(square)
    return available_squares


def available_squares_queen(origin: Square, piece_dict) -> [Square]:
    """
    A queen moves in line and diagonal, and can't go threw another piece,
    but can take a piece with a different color.
    @return: list of reachable squares
    """
    available_squares: list[Square] = []
    # right squares
    available_squares.extend(
        available_squares_on_right(
            origin,
            piece_dict,
        )
    )
    # left squares
    available_squares.extend(
        available_squares_on_left(
            origin,
            piece_dict,
        )
    )
    # up squares
    available_squares.extend(
        available_squares_upper(
            origin,
            piece_dict,
        )
    )
    # down squares
    available_squares.extend(
        available_squares_below(
            origin,
            piece_dict,
        )
    )
    # diagonal right up squares
    available_squares.extend(
        available_squares_diagonal_right_up(
            origin,
            piece_dict,
        )
    )
    # diagonal right down squares
    available_squares.extend(
        available_squares_diagonal_right_down(
            origin,
            piece_dict,
        )
    )
    # diagonal left up squares
    available_squares.extend(
        available_squares_diagonal_left_up(
            origin,
            piece_dict,
        )
    )
    # diagonal left down squares
    available_squares.extend(
        available_squares_diagonal_left_down(
            origin,
            piece_dict,
        )
    )
    return available_squares


def available_squares_rook(origin: Square, piece_dict) -> [Square]:
    """
    A rook moves in line, and can't go threw another piece,
    but can take a piece with a different color.
    @param piece_dict: {(Column, row): Piece} dict of the pieces in the game
    @return: list of reachable squares
    """
    available_squares: list[Square] = []
    # right squares
    available_squares.extend(
        available_squares_on_right(
            origin,
            piece_dict,
        )
    )
    # left squares
    available_squares.extend(
        available_squares_on_left(
            origin,
            piece_dict,
        )
    )
    # up squares
    available_squares.extend(
        available_squares_upper(
            origin,
            piece_dict,
        )
    )
    # down squares
    available_squares.extend(
        available_squares_below(
            origin,
            piece_dict,
        )
    )
    return available_squares
