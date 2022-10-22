"""
Test tht it is possible to get the king moves
"""
from app.src.model.classes.pieces.king import King
from app.src.model.classes.pieces.pawn import Pawn
from app.src.model.classes.pieces.piece import Piece
from app.src.model.classes.pieces.rook import Rook
from app.src.model.classes.square import Square
from app.src.model.events.moves.king_move import KingMove
from app.src.model.events.moves.long_castling import LongCastling
from app.src.model.events.moves.rook_move import RookMove
from app.src.model.events.moves.short_castling import ShortCastling
from app.src.model.game.board import Board
from app.src.model.game.game import Game
from app.src.model.miscenaleous.color import Color
from app.src.model.miscenaleous.column import Column
from app.src.model.miscenaleous.utils import square_available_moves_no_castling

short_castle = ShortCastling(Square(Column.E, 1))
long_castle = LongCastling(Square(Column.E, 1))


def test_available_king_moves():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | |p|K|P| | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | | | | | |
       A B C D E F G H
    No need to do extensive tests, since they are done in the Piece tests
    (The rook moves uses _available_square_on_side_line, already completely
    tested)
    @return:
    """
    piece_dict = {
        Square(Column.D, 4): King(Color.WHITE),
        Square(Column.E, 4): Pawn(Color.WHITE),
        Square(Column.C, 4): Pawn(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    expected_moves = [
        KingMove(Square(Column.D, 4), Square(Column.C, 3)),
        KingMove(Square(Column.D, 4), Square(Column.C, 4)),
        KingMove(Square(Column.D, 4), Square(Column.C, 5)),
        KingMove(Square(Column.D, 4), Square(Column.D, 3)),
        KingMove(Square(Column.D, 4), Square(Column.D, 5)),
        KingMove(Square(Column.D, 4), Square(Column.E, 3)),
        KingMove(Square(Column.D, 4), Square(Column.E, 5)),
    ]
    assert (
        square_available_moves_no_castling(Square(Column.D, 4), board) == expected_moves
    )


def test_is_short_castling_available():
    """
    | | | | |K|x|x|R|
     A B C D E F G H
    Check that a valid set up return the square
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert short_castle in game.square_available_moves(Square(Column.E, 1))


def test_is_short_castling_not_available1():
    """
    | | | | | | | |R|
    | | | | |K|x|x| |
     A B C D E F G H
    Check that if the rook has moved, castling unavailable
    Check that if there is no rook, castling is unavailable
    @return:
    """
    # no rook
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
        Square(Column.A, 1): King(Color.BLACK),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    game.apply_move(RookMove(Square(Column.H, 1), Square(Column.H, 2)))
    assert short_castle not in game.square_available_moves(Square(Column.E, 1))
    game.game_state.player = Color.WHITE
    # rook has moved
    game.apply_move(RookMove(Square(Column.H, 2), Square(Column.H, 1)))
    assert short_castle not in game.square_available_moves(Square(Column.E, 1))


def test_is_short_castling_not_available12():
    """
    Check that if the king has moved, castling unavailable
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
        Square(Column.A, 6): King(Color.BLACK),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    game.apply_move(KingMove(Square(Column.E, 1), Square(Column.E, 2)))
    assert short_castle not in game.square_available_moves(Square(Column.E, 2))


def test_is_short_castling_not_available13():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 |r| | | |K| | |R|
       A B C D E F G H
    Check that if the king is in check, castling unavailable
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
        Square(Column.A, 1): Rook(Color.BLACK),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert short_castle not in game.square_available_moves(Square(Column.E, 1))


def test_is_short_castling_not_available14():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 | | | | |K|W|W|R|
       A B C D E F G H
    Check that if the F column is not empty, castling unavailable
    Check that if the G column is not empty, castling unavailable
    @return:
    """
    # F not empty
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
        Square(Column.F, 1): Piece(Color.WHITE),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert short_castle not in game.square_available_moves(Square(Column.E, 1))
    # G not empty
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
        Square(Column.G, 1): Piece(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert short_castle not in game.square_available_moves(Square(Column.E, 1))


def test_is_short_castling_not_available15():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | |r|r| |
    1 | | | | |K| | |R|
       A B C D E F G H
    Check that if the F column is in check, castling unavailable
    Check that if the G column is in check, castling unavailable
    @return:
    """
    # Column F in check
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
        Square(Column.F, 2): Rook(Color.BLACK),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert short_castle not in game.square_available_moves(Square(Column.E, 1))
    # Column G in check
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.H, 1): Rook(Color.WHITE),
        Square(Column.G, 2): Rook(Color.BLACK),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert short_castle not in game.square_available_moves(Square(Column.E, 1))


def test_is_long_castling_available():
    """
    |R| | | |K| | | |
     A B C D E F G H
    Check that a valid set-up return the square
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
        Square(Column.B, 2): Rook(Color.BLACK),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert long_castle in game.square_available_moves(Square(Column.E, 1))


def test_is_long_castling_not_available1():
    """
    |R| | | | | | | |
    | | | | |K|x|x| |
     A B C D E F G H
    Check that if the rook has moved, castling unavailable
    Check that if there is no rook, castling is unavailable
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
        Square(Column.H, 7): King(Color.BLACK),

    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    game.apply_move(RookMove(Square(Column.A, 1), Square(Column.A, 2)))
    assert long_castle not in game.square_available_moves(Square(Column.E, 1))
    game.game_state.player = Color.WHITE
    # rook has moved
    game.apply_move(RookMove(Square(Column.A, 2), Square(Column.A, 1)))
    assert long_castle not in game.square_available_moves(Square(Column.E, 1))


def test_is_long_castling_not_available12():
    """
    Check that if the king has moved, castling unavailable
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
        Square(Column.H, 7): King(Color.BLACK),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    game.apply_move(KingMove(Square(Column.E, 1), Square(Column.E, 2)))
    assert long_castle not in game.square_available_moves(Square(Column.E, 2))


def test_is_long_castling_not_available13():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 |R| | | |K| | |B|
       A B C D E F G H
    Check that if the king is in check, castling unavailable
    @return:
    """
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
        Square(Column.H, 1): Rook(Color.BLACK),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert long_castle not in game.square_available_moves(Square(Column.E, 1))


def test_is_long_castling_not_available14():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | | | | | | | |
    1 |R|W|W|W|K| | | |
       A B C D E F G H
    Check that if the B column is not empty, castling unavailable
    Check that if the C column is not empty, castling unavailable
    Check that if the D column is not empty, castling unavailable
    @return:
    """
    # B not empty
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
        Square(Column.B, 1): Piece(Color.WHITE),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert long_castle not in game.square_available_moves(Square(Column.E, 1))

    # C not empty
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
        Square(Column.C, 1): Piece(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert long_castle not in game.square_available_moves(Square(Column.E, 1))

    # D not empty
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
        Square(Column.D, 1): Piece(Color.WHITE),
    }
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert long_castle not in game.square_available_moves(Square(Column.E, 1))


def test_is_long_castling_not_available15():
    """
    8 | | | | | | | | |
    7 | | | | | | | | |
    6 | | | | | | | | |
    5 | | | | | | | | |
    4 | | | | | | | | |
    3 | | | | | | | | |
    2 | | |b|b| | | | |
    1 |R| | | |K| | | |
       A B C D E F G H
    Check that if the C column is in check, castling unavailable
    Check that if the D column is in check, castling unavailable
    @return:
    """
    # Column C in check
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
        Square(Column.C, 2): Rook(Color.BLACK),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert long_castle not in game.square_available_moves(Square(Column.E, 1))

    # Column D in check
    piece_dict = {
        Square(Column.E, 1): King(Color.WHITE),
        Square(Column.A, 1): Rook(Color.WHITE),
        Square(Column.D, 2): Rook(Color.BLACK),
    }
    game = Game()
    board = Board()
    board.piece_dict = piece_dict
    game.board = board
    assert long_castle not in game.square_available_moves(Square(Column.E, 1))
