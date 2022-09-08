"""
Abstract class for movements
"""
from abc import ABC, abstractmethod

from app.src.model.game.square import Square
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.pieces.piece import Piece


class Move(ABC):
    """
    Abstract class
    """

    def __init__(
        self,
        origin: Square,
        destination: Square,
    ):
        """
        Constructor
        @param origin: origin square
        @param destination: destination square
        """
        self.origin = origin
        self.destination = destination

    def is_legal(
        self,
        piece_dict: dict[Square, Piece],
    ) -> bool:
        """
        Return a boolean value indicating whether the move is legal or not.
        @return:
        """

    def apply_move(self):
        """
        Apply a move
        Moves the piece.
        @return:
        """

    def __eq__(self, other):
        return (
            self.origin == other.origin
            and self.destination == other.destination
            and type(other) == type(self)
        )

    def __repr__(self):
        return f"{self.origin.column.name}{self.origin.row}" \
               f"{self.destination.column.name}{self.destination.row}"

    @staticmethod
    @abstractmethod
    def get_available_moves(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        """
        Return a list of the available moves from origin
        @param piece_dict:
        @param origin: origin square
        @return:
        """

    @staticmethod
    def _get_current_color(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ) -> Color:
        """
        Get the color of the current player, with the piece list and the coordinates
        @return:
        """
        return piece_dict[origin].color

    @staticmethod
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
        color = Move._get_current_color(origin, piece_dict)
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

    @staticmethod
    def _available_squares_on_right(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        """
        Returns the available squares on the right on the piece
        @param piece_dict: {(Column, row): Piece} dict of the pieces in the game
        @return:
        """
        return Move._available_square_on_side_line(
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

    @staticmethod
    def _available_squares_on_left(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        """
        Returns the available squares on the right on the piece

        """
        return Move._available_square_on_side_line(
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

    @staticmethod
    def _available_squares_upper(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        """
        Returns the available squares on the right on the piece
        @return:
        """
        return Move._available_square_on_side_line(
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

    @staticmethod
    def _available_squares_below(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        """
        Returns the available squares on the right on the piece
        @return:
        """
        return Move._available_square_on_side_line(
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

    @staticmethod
    def _available_squares_diagonal_right_up(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        """
        Returns the available squares on the right on the piece
        @return:
        """
        return Move._available_square_on_side_line(
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

    @staticmethod
    def _available_squares_diagonal_right_down(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        """
        Returns the available squares on the right on the piece
        @return:
        """
        return Move._available_square_on_side_line(
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

    @staticmethod
    def _available_squares_diagonal_left_up(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        """
        Returns the available squares on the right on the piece
        @return:
        """
        return Move._available_square_on_side_line(
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

    @staticmethod
    def _available_squares_diagonal_left_down(
        origin: Square,
        piece_dict: dict[Square, Piece],
    ):
        """
        Returns the available squares on the right on the piece
        @return:
        """
        return Move._available_square_on_side_line(
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
