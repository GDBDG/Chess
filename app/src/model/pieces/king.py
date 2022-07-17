"""
Implementation of the king
Check if the king is in check
Castling :
"""
from copy import copy
from typing import Optional

from app.src.exceptions.invalid_movement_error import InvalidMovementError
from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.castling_errors import CastlingErrors
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.move import Move, ShortCastling, LongCastling
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.pieces.piece import Piece


class King(Piece):
    """
    Implementation of king
    """

    piece_type = PieceType.KING

    def available_squares(self, square_list, piece_list) -> [Square]:
        """
        A king can move like a queen, but only of one square
        Can't be in check (makes the verification)
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: list of reachable squares
        """
        available_squares = self.available_squares_to_capture(square_list, piece_list)
        # Remove the squares if the king is in check
        for square in copy(available_squares):
            if Piece.is_square_in_check(
                    self.color,
                    square,
                    square_list,
                    piece_list,
            ):
                available_squares.remove(square)

        return available_squares

    def available_moves(
            self, square_list, piece_list, _: Optional[Move] = None
    ) -> [Move]:
        available_moves = super().available_moves(square_list, piece_list)
        if (
                self.is_short_castling_valid(square_list, piece_list)
                == CastlingErrors.VALID
        ):
            available_moves.append(
                ShortCastling(
                    square_list[self.column, self.row], square_list[Column.H, self.row]
                )
            )
        if self.is_long_castling_valid(square_list, piece_list) == CastlingErrors.VALID:
            available_moves.append(
                LongCastling(
                    square_list[self.column, self.row], square_list[Column.C, self.row]
                )
            )
        return available_moves

    def available_squares_to_capture(self, square_list, piece_list) -> [Square]:
        available_squares: list[Square] = []
        # Add the squares
        Piece._add_square(
            self.column.value - 1,
            self.row - 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value - 1,
            self.row,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value - 1,
            self.row + 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value,
            self.row - 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value,
            self.row + 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value + 1,
            self.row - 1,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value + 1,
            self.row,
            square_list,
            available_squares,
        )
        Piece._add_square(
            self.column.value + 1,
            self.row + 1,
            square_list,
            available_squares,
        )
        # Remove the squares if there is a piece on the same color
        for square in copy(available_squares):
            if (square.column, square.row) in piece_list and piece_list[
                square.column, square.row
            ].color == self.color:
                available_squares.remove(square)

        return available_squares

    def is_short_castling_valid(self, square_list, piece_list):
        """
        | | | | |K|x|x|R|
         A B C D E F G H
        neither the king nor the rook has moved
        the king is not in check
        x must be empty,
        x must not be in check
        (no need to check the position, since the king has not moved)

        Check if the king can make a short castling,
        and return the square destination
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: bool
        """
        row = self.row
        # check the rook is still here, and hasn't moved
        if (Column.H, row) not in piece_list or piece_list[Column.H, row].has_moved:
            return CastlingErrors.ROOK_HAS_MOVED
        # check if the king has not moved
        if self.has_moved:
            return CastlingErrors.KING_HAS_MOVED
        # check if the king is not in check
        if self.is_in_check(square_list, piece_list):
            return CastlingErrors.KING_IN_CHECK
        # check if x are empty
        if (Column.F, row) in piece_list or (Column.G, row) in piece_list:
            return CastlingErrors.NOT_EMPTY_PATH
        # check if x are not in check
        if Piece.is_square_in_check(
                self.color,
                square_list[(Column.F, row)],
                square_list,
                piece_list,
        ) or Piece.is_square_in_check(
            self.color,
            square_list[(Column.G, row)],
            square_list,
            piece_list,
        ):
            return CastlingErrors.PATH_IN_CHECK
        return CastlingErrors.VALID

    def is_long_castling_valid(self, square_list, piece_list):
        """
        |R|x|X|X|K| | | |
         A B C D E F G H
        neither the king nor the rook has moved
        the king is not in check
        x and X must be empty,
        X must not be in check
        (no need to check the position, since the king has not moved)

        Check if the king can make a short castling,
        and return the square destination
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: square destination if available, else None
        """
        row = self.row
        # check the rook is still here, and hasn't moved
        if (Column.A, row) not in piece_list or piece_list[Column.A, row].has_moved:
            return CastlingErrors.ROOK_HAS_MOVED
        # check if the king has not moved
        if self.has_moved:
            return CastlingErrors.KING_HAS_MOVED
        # check if the king is not in check
        if self.is_in_check(square_list, piece_list):
            return CastlingErrors.KING_IN_CHECK
        # check if x are empty
        if (
                (Column.D, row) in piece_list
                or (Column.C, row) in piece_list
                or (Column.B, row) in piece_list
        ):
            return CastlingErrors.NOT_EMPTY_PATH
        # check if X are not in check
        if Piece.is_square_in_check(
                self.color,
                square_list[(Column.D, row)],
                square_list,
                piece_list,
        ) or Piece.is_square_in_check(
            self.color,
            square_list[(Column.C, row)],
            square_list,
            piece_list,
        ):
            return CastlingErrors.PATH_IN_CHECK
        return CastlingErrors.VALID

    def short_castle(self, square_list, piece_list):
        """
        Apply the short Castle
        * Move the king
        * Move the rook (the piece_list must contain the real pieces, and not a copy)
        Raises an error if the short castling is unavailable
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        message = self.is_short_castling_valid(square_list, piece_list)
        # If castling invalid
        if message != CastlingErrors.VALID:
            raise InvalidMovementError(
                square_list[self.column, self.row],
                f"Short castle unavailable\n{message}",
            )
        # Moves the king
        piece_list.pop(
            (self.column, self.row),
        )
        self.column = Column.G
        self.has_moved = True
        piece_list[self.column, self.row] = self
        # Moves the Rook
        rook = piece_list[Column.H, self.row]
        piece_list.pop(
            (Column.H, self.row),
        )
        rook.column = Column.F
        rook.has_moved = True
        piece_list[Column.F, self.row] = rook

    def long_castle(self, square_list, piece_list):
        """
        Apply the long Castle
        * Move the king
        * Move the rook (the piece_list must contain the real pieces, and not a copy)
        Raises an error if the short castling is unavailable
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        message = self.is_long_castling_valid(square_list, piece_list)
        # If castling invalid
        if message != CastlingErrors.VALID:
            raise InvalidMovementError(
                square_list[self.column, self.row],
                f"Long castle unavailable\n{message}",
            )
        # Moves the king
        piece_list.pop(
            (self.column, self.row),
        )
        self.column = Column.C
        self.has_moved = True
        piece_list[self.column, self.row] = self
        # Moves the Rook
        rook = piece_list[Column.A, self.row]
        piece_list.pop(
            (Column.A, self.row),
        )
        rook.column = Column.D
        rook.has_moved = True
        piece_list[Column.F, self.row] = rook

    def apply_move(self, move: Move, square_list, piece_list,_: Optional[Move] = None):
        """
        Apply moves like super, but also Castling
        :param _:
        :param move: move to apply
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: None
        """
        if type(move) == ShortCastling and self.is_short_castling_valid(square_list, piece_list):
            self.short_castle(square_list, piece_list)
        elif type(move) == LongCastling and self.is_long_castling_valid(square_list, piece_list):
            self.long_castle(square_list, piece_list)
        else:
            super().apply_move(move, square_list, piece_list)
