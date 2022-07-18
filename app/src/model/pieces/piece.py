"""
Piece classes
"""
from copy import deepcopy
from typing import Optional

from app.src.exceptions.invalid_move_error import InvalidMoveError
from app.src.exceptions.invalid_movement_error import InvalidMovementError
from app.src.exceptions.missing_king_error import MissingKingError
from app.src.exceptions.row_error import RowError
from app.src.model.chess_board.square import Square
from app.src.model.constantes import ILLEGAL_MOVE_MESSAGE
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.move import Move
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.miscenaleous.utils import get_king


class Piece:
    """
    Generic class of a chess piece.
    Has no gaming meaning, but contains methods for all pieces
    """

    piece_type = PieceType.PIECE

    def __init__(self, column: Column, row: int, color: Color = Color.WHITE):
        """
        Constructor of piece
        :param row: between 1 and 8, row coordinate
        :param column: between A and H (Column enum),
        :param color:
        """
        if not 1 <= row <= 8:
            raise RowError(row)
        self.column = column
        self.row = row
        self.color = color
        self.has_moved = False

    @staticmethod
    def _add_square(
        column: int, row: int, square_list, available_squares: [Square]
    ) -> [Square]:
        """
        Add the square with coordinates column and row in available_squares
        if it is in square_list
        :param row: row coordinate int value
        :param column: column coordinate (int value)
        :param square_list: {(col, row): Square} dict of the squares present in the game
        :param available_squares: list of square where the square will be added
        :return: available_squares
        """
        try:
            column = Column(column)
        except ValueError:
            pass
        else:
            if (column, row) in square_list:
                available_squares.append(square_list[column, row])
        return available_squares

    @staticmethod
    def is_square_in_check(
        color: Color, square: Square, square_list, piece_list
    ) -> bool:
        """
        Return a boolean indicating if a piece in a different color can move
        to square (indicates if a piece of color *color* is in check)
        :param color: color of the piece that we check if it can be taken
        :param square: the square where we check if it can be taken
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: boolean
        """
        return any(
            piece.color != color
            and square in piece.available_squares_to_capture(square_list, piece_list)
            for piece in piece_list.values()
        )

    def is_in_check(self, square_list, piece_list) -> bool:
        """
        Return a boolean indicating if a piece in a different color can move
        to square (indicates if a piece of color *color* is in check)
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: boolean
        """
        return any(
            piece.color != self.color
            and square_list[self.column, self.row]
            in piece.available_squares_to_capture(square_list, piece_list)
            for piece in piece_list.values()
        )

    def available_squares(self, square_list, piece_list) -> [Square]:
        """
        Return all squares empty or with a piece in the opposite team,
        :return: list of Square
        """
        return [
            square
            for square in square_list.values()
            if ((square.column, square.row) not in piece_list.keys())
            or piece_list[(square.column, square.row)].color != self.color
        ]

    def _available_moves_no_legal_verification(
        self, square_list, piece_list, _: Move
    ) -> [Move]:
        """
        Return a list of available moves (does NOT check if the move is legal)
        :param _:
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: A list of the moves
        """
        return list(
            map(
                lambda x: Move(
                    square_list[self.column, self.row],
                    square_list[x.column, x.row],
                    self.piece_type,
                ),
                self.available_squares(square_list, piece_list),
            )
        )

    def available_moves(self, square_list, piece_list, last_move: Move) -> [Move]:
        """
        Return a list of available moves (CHECK if the move is legal)
        :param last_move:
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: A list of the moves
        """
        return [
            move
            for move in self._available_moves_no_legal_verification(
                square_list, piece_list, last_move
            )
            if self.is_move_legal(move, last_move, square_list, piece_list)
        ]

    def available_squares_to_capture(self, square_list, piece_list) -> [Square]:
        """
        Return all squares where a piece can capture an opposite piece
        Same as available_squares, except for the pawn
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:  square list
        """
        return self.available_squares(square_list, piece_list)

    def move_to(self, destination: Square, square_list, piece_list):
        """
        Move the piece to a new square
        * Checks if the square is available
        * update piece list
        :param destination: instance of Square where self is moved
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: None
        """
        # Raises an exception if the asked destination is not available
        if destination not in self.available_squares(square_list, piece_list):
            raise InvalidMovementError(destination)
        # Remove older piece in piece list
        piece_list.pop((self.column, self.row))
        # Set new coordinates
        self.row = destination.row
        self.column = destination.column
        self.has_moved = True
        # Add new piece in piece_list
        piece_list[self.column, self.row] = self

    def is_move_legal(
        self, move: Move, last_move: Move, square_list, piece_list
    ) -> bool:
        """
        Return a boolean saying if a move is Legal.
        (Plays the move, and check the king is not in check)
        :param last_move:
        :param move: Move instance,
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: boolean saying if move is legal
        """
        # Virtually play the move
        piece_list_copy = deepcopy(piece_list)
        piece_copy = deepcopy(self)
        piece_list_copy[piece_copy.column, piece_copy.row] = piece_copy
        try:
            piece_copy._apply_move_no_legal_verification(
                move, square_list, piece_list_copy, last_move
            )
        except InvalidMoveError as error:
            raise error
        if piece_copy.piece_type == PieceType.KING:
            king = piece_copy
        # Check that the king is not in check
        else:
            try:
                king = get_king(piece_list_copy, self.color)
            except MissingKingError as error:
                raise error
        return not king.is_in_check(square_list, piece_list_copy)

    def _apply_move_no_legal_verification(
        self, move: Move, square_list, piece_list, last_move: Move
    ):
        """
        Apply the move if it is valid, else raises an error
        Does NOT verify that the move is legal
        :param _:
        :param move: move to apply
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: None
        """
        if type(move) != Move:
            raise InvalidMoveError(move)
        if move.piece_type != self.piece_type:
            raise InvalidMoveError(move)
        if move not in self._available_moves_no_legal_verification(
            square_list, piece_list, last_move
        ):
            raise InvalidMoveError(move)
        self.move_to(move.destination, square_list, piece_list)

    def apply_move(
        self, move: Move, square_list, piece_list, last_move: Optional[Move] = None
    ):
        """
        Apply the move if it is valid, else raises an error
        :param last_move:
        :param move: move to apply
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: None
        """
        if not self.is_move_legal(move, last_move, square_list, piece_list):
            raise InvalidMoveError(move, ILLEGAL_MOVE_MESSAGE)
        self._apply_move_no_legal_verification(move, square_list, piece_list, last_move)

    def _available_square_on_side_line(
        self,
        columns: [Column],
        rows: [int],
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on only one side.@
        (for ex on the right side, or diagonal right).
        Take a list of rows and a list of columns, and iterate on the squares
        with these coordinates.
        columns and rows must have the same size.
        :param columns: list of column to iterate on,
        :param rows: list of rows to iterate on
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: list of pieces (represents the pieces in the game)
        :return: square_list of available squares designated by th product of columns and rows
        """
        available_squares = []
        for column, row in zip(columns, rows):
            # if there is a piece on the square
            if (column, row) in piece_list:
                # if the piece can take the other piece
                if piece_list[column, row].color != self.color:
                    available_squares.append(square_list[column, row])
                break
            # if there is no piece on the square
            available_squares.append(square_list[column, row])
        return available_squares

    def _available_squares_on_right(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        return self._available_square_on_side_line(
            map(Column, range(self.column.value + 1, 9)),
            [self.row] * (8 - self.column.value),
            square_list,
            piece_list,
        )

    def _available_squares_on_left(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        return self._available_square_on_side_line(
            map(Column, range(self.column.value - 1, 0, -1)),
            [self.row] * (self.column.value - 1),
            square_list,
            piece_list,
        )

    def _available_squares_upper(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        return self._available_square_on_side_line(
            [self.column] * (8 - self.row),
            range(self.row + 1, 9),
            square_list,
            piece_list,
        )

    def _available_squares_below(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        return self._available_square_on_side_line(
            [self.column] * (self.row - 1),
            range(self.row - 1, 0, -1),
            square_list,
            piece_list,
        )

    def _available_squares_diagonal_right_up(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        return self._available_square_on_side_line(
            map(Column, range(self.column.value + 1, 9)),
            range(self.row + 1, 9),
            square_list,
            piece_list,
        )

    def _available_squares_diagonal_right_down(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        return self._available_square_on_side_line(
            map(Column, range(self.column.value + 1, 9)),
            range(self.row - 1, 0, -1),
            square_list,
            piece_list,
        )

    def _available_squares_diagonal_left_up(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        return self._available_square_on_side_line(
            map(Column, range(self.column.value - 1, 0, -1)),
            range(self.row + 1, 9),
            square_list,
            piece_list,
        )

    def _available_squares_diagonal_left_down(
        self,
        square_list,
        piece_list,
    ):
        """
        Returns the available squares on the right on the piece
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        return self._available_square_on_side_line(
            map(Column, range(self.column.value - 1, 0, -1)),
            range(self.row - 1, 0, -1),
            square_list,
            piece_list,
        )
