"""
Implementation of bishop
moves in line, no piece in trajectory
"""
from app.src.model.chess_board.square import Square
from app.src.model.miscenaleous.piece_type import PieceType
from app.src.model.pieces.piece import Piece


class Bishop(Piece):
    """
    Bishop class
    """

    piece_type = PieceType.BISHOP

    def available_squares(self, square_list, piece_list) -> [Square]:
        """
        A bishop moves in diagonal, and can't go threw another piece,
        Can take piece with different color
        :param square_list: {(column, row): Square} dict of the squares in the game
        :param piece_list: {(Column, row): Piece} dict of the pieces in the game
        :return: list of reachable squares
        """
        available_squares: list[Square] = []
        # diagonal right up squares
        available_squares.extend(
            self._available_squares_diagonal_right_up(
                square_list,
                piece_list,
            )
        )
        # diagonal right down squares
        available_squares.extend(
            self._available_squares_diagonal_right_down(
                square_list,
                piece_list,
            )
        )
        # diagonal left up squares
        available_squares.extend(
            self._available_squares_diagonal_left_up(
                square_list,
                piece_list,
            )
        )
        # diagonal left down squares
        available_squares.extend(
            self._available_squares_diagonal_left_down(
                square_list,
                piece_list,
            )
        )
        return available_squares
