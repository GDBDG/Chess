"""
Implementation of rook
move in line, no piece in trajectory
"""
from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.pieces.piece import Piece


class Rook(Piece):
    """
    Rook class
    """

    piece_type = PieceType.ROOK

    def available_squares(self, square_list, piece_list) -> [Square]:
        """
        A rook move in line, and can't go threw another piece,
        but can take a piece with a different color.
        @param square_list: {(column, row): Square} dict of the squares in the game
        @param piece_list: {(Column, row): Piece} dict of the pieces in the game
        @return: list of reachable squares
        """
        available_squares: list[Square] = []
        # right squares
        available_squares.extend(
            self._available_squares_on_right(
                square_list,
                piece_list,
            )
        )
        # left squares
        available_squares.extend(
            self._available_squares_on_left(
                square_list,
                piece_list,
            )
        )
        # up squares
        available_squares.extend(
            self._available_squares_upper(
                square_list,
                piece_list,
            )
        )
        # down squares
        available_squares.extend(
            self._available_squares_below(
                square_list,
                piece_list,
            )
        )
        return available_squares
