"""
Queen
Move in line and diagonal
"""
from app.src.back.chess_board.square import Square
from app.src.back.pieces.piece import Piece


class Queen(Piece):
    """
    Queen class
    """

    def available_squares(self, square_list, piece_list) -> [Square]:
        """
        A queen move in line and diagonal, and can't go threw another piece,
        but can take a piece with a different color.
        :param square_list: list of available squares
        :param piece_list: list of others pieces in the game
        :return: list of reachable squares
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
