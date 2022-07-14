"""
PAWN :
A pawn moves straight forward one square, if that square is vacant.
If it has not yet moved, a pawn also has the option of moving two squares straight forward,
provided both squares are vacant. Pawns cannot move backwards.
A pawn, unlike other pieces, captures differently from how it moves.
A pawn can capture an enemy piece on either of the two squares diagonally in front of the pawn.
It cannot move to those squares when vacant except when capturing en passant.
En passant :
Promotion :
"""
from typing import Optional

from app.src.back.chess_board.square import Square
from app.src.back.miscenaleous.color import Color
from app.src.back.miscenaleous.column import Column
from app.src.back.miscenaleous.move import Move
from app.src.back.pieces.piece import Piece
from app.src.exceptions.invalid_movement_error import (
    InvalidMovementError,
    EN_PASSANT_UNAVAILABLE_MESSAGE,
)


class Pawn(Piece):
    """
    White pawn class
    """

    def _next_row(self, step: int = 1) -> int:
        """
        Return the net row, depending on the color of the piece, and the step
        row +1/+2 if color = White, row -1/-2 if color = black
        :param step: number of rows the pawn moves
        :return:
        """
        return self.row + step * (
            (self.color == Color.WHITE) - (self.color == Color.BLACK)
        )

    def available_squares_to_capture(self, square_list, piece_list) -> [Square]:
        """
        Return all squares where a piece can capture an opposite piece
        Same as available_squares, except for the pawn
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:  square list
        """
        available_squares = []
        # capture on right
        if (
            Column(self.column.value + 1),
            self._next_row(),
        ) in piece_list and piece_list[
            Column(self.column.value + 1), self._next_row()
        ].color != self.color:
            available_squares.append(
                square_list[(Column(self.column.value + 1), self._next_row())]
            )
        # capture on left
        if (
            Column(self.column.value - 1),
            self._next_row(),
        ) in piece_list and piece_list[
            Column(self.column.value - 1), self._next_row()
        ].color != self.color:
            available_squares.append(
                square_list[(Column(self.column.value - 1), self._next_row())]
            )
        return available_squares

    def available_squares(self, square_list, piece_list) -> [Square]:
        """
        Return the available squares for a pawn (not the en passant)
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        """
        available_squares = self.available_squares_to_capture(square_list, piece_list)
        # forward (vacant)
        if (self.column, self._next_row()) not in piece_list:
            available_squares.append(square_list[self.column, self._next_row()])
        # first movement
        if (
            not self.has_moved
            and (self.column, self._next_row()) not in piece_list
            and (self.column, self._next_row(2)) not in piece_list
        ):
            available_squares.append(square_list[self.column, self._next_row(2)])
        return available_squares

    def en_passant_available_destination(
        self, square_list, last_move: Move
    ) -> Optional[Square]:
        """
        8 | | | | | | | | |
        7 | | | | | | | | |
        6 | | | | | |x| | |
        5 | | | | | |B|W| |
        4 | |W|B| | | | | |
        3 | | |x| | | | | |
        2 | | | | | | | | |
        1 | | | | | | | | |
           A B C D E F G H
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param last_move: Move, last_move played move in the game
        :return: Square destination if en passant is available, None else
        """
        if (
            last_move.allow_en_passant()
            and self.row == last_move.destination.row
            and abs(self.column.value - last_move.destination.column.value) == 1
        ):
            return square_list[last_move.destination.column, self._next_row()]
        return None

    def en_passant(self, square_list, piece_list, last_move: Move):
        """
        Execute en passant capture
        raises an error if the destination is invalid
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return:
        :param last_move:
        :return:
        """
        destination = self.en_passant_available_destination(square_list, last_move)
        if destination is None:
            raise InvalidMovementError(None, EN_PASSANT_UNAVAILABLE_MESSAGE)
        # Remove older piece in piece list
        piece_list.pop((self.column, self.row))
        # Set new coordinates
        self.row = self._next_row()
        self.column = destination.column
        # Add new piece in piece_list
        piece_list[self.column, self.row] = self
        # Delete the other pawn
        piece_list.pop((last_move.destination.column, last_move.destination.row))
