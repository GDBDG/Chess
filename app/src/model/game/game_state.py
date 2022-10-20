"""
State (running, draw)
Associated methods, (state update and getter)
"""
from app.src.model.game.game_historic import GameHistoric
from app.src.model.miscenaleous.color import Color
from app.src.model.move.pawn_move import PawnMove


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

    def update_state(self, game_historic: GameHistoric, capture: bool):
        """
        Update the counter for the '50-moves' rule
        @param game_historic:
        @param capture: boolean value if the last move was a capture
        @return:
        """
        if capture or isinstance(game_historic.move_historic[-1], PawnMove):
            self.fifty_counter = 0
        else:
            self.fifty_counter += 1
            if self.fifty_counter == 100:
                self.state = GameState.DRAW
        # Dead position
        # TODO
        # Threefold rule
        if 3 in game_historic.config_historic.values():
            self.state = GameState.DRAW
        # Update the player who has to play
        self.player = Color.BLACK if self.player == Color.WHITE else Color.WHITE
