"""
State (running, draw)
Associated methods, (state update and getter)
"""
from src.CHESS.domain.classes.const.color import Color
from src.CHESS.domain.classes.pieces.bishop import Bishop
from src.CHESS.domain.classes.pieces.king import King
from src.CHESS.domain.classes.pieces.knight import Knight
from src.CHESS.domain.classes.pieces.pawn import Pawn
from src.CHESS.domain.classes.pieces.queen import Queen
from src.CHESS.domain.classes.pieces.rook import Rook
from src.CHESS.domain.events.moves.pawn_move import PawnMove
from src.CHESS.domain.states.board import Board
from src.CHESS.domain.states.game_historic import GameHistoric


class GameState:
    """
    Game state
    Manage state (running, draw, win)
    Manage draw rules
    """

    RUNNING = "running"
    WHITE_WIN = "+/-"
    BLACK_WIN = "-/+"
    DRAW = "-/-"

    def __init__(self):
        """
        Constructor
        """
        self.state = GameState.RUNNING
        self.fifty_counter = 0
        self.player = Color.WHITE

    def fifty_move_rule(self, game_historic: GameHistoric, capture: bool):
        """
        Update the counter for the '50-moves' rule
        @param game_historic:
        @param capture: boolean, if the last move is a capture or not
        @return:
        """
        if capture or isinstance(game_historic.move_historic[-1], PawnMove):
            self.fifty_counter = 0
        else:
            self.fifty_counter += 1
            if self.fifty_counter == 100:
                self.state = GameState.DRAW

    def three_fold_rule(self, game_historic: GameHistoric):
        """
        Update the three-fold state
        @return:
        """
        if 3 in game_historic.config_historic.values():
            self.state = GameState.DRAW

    def dead_position_rule(self, board: Board):
        """
        Update the state for the dead positions rule
        @param board:
        @return:
        """
        piece_counter = board.get_piece_type_counter()
        dead_position_boards = [
            {Bishop: 0, King: 2, Knight: 0, Pawn: 0, Queen: 0, Rook: 0},
            {Bishop: 1, King: 2, Knight: 0, Pawn: 0, Queen: 0, Rook: 0},
            {Bishop: 0, King: 2, Knight: 1, Pawn: 0, Queen: 0, Rook: 0},
        ]
        if piece_counter in dead_position_boards:
            self.state = GameState.DRAW
        if (
            piece_counter == {Bishop: 2, King: 2, Knight: 0, Pawn: 0, Queen: 0, Rook: 0}
            and board.are_bishop_in_dead_position()
        ):
            self.state = GameState.DRAW

    def update_state(self, game_historic: GameHistoric, capture: bool):
        """
        Update the state for all rules
        @param game_historic:
        @param capture: boolean value if the last moves was a capture
        @return:
        """
        self.fifty_move_rule(game_historic, capture)
        self.three_fold_rule(game_historic)
        # pylint: disable=W0511
        # Dead position
        # TODO

        # Update the player who has to play
        self.player = Color.BLACK if self.player == Color.WHITE else Color.WHITE
