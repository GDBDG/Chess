"""
Historic of a game
* played moves
* hashes of the config
"""

from app.src.model.events.moves.empty_move import EmptyMove
from app.src.model.events.moves.move import Move
from app.src.model.game.board import Board


class GameHistoric:
    """
    Contain previous states information
    """

    def __init__(self):
        """
        Constructor
        """
        self.move_historic: [Move] = [EmptyMove()]
        self.config_historic = {}

    def update_historic(self, move: Move, board: Board):
        """
        Update the configuration history
        Use a custom hash from the piece_dict
        a square state is encoded on 4 bits abcd
        a: 1 if white, 0 other
        bcd: 001 : bishop 9 | 1
        bcd: 010 : king  a | 2
        bcd: 011 : knight b | 3
        bcd: 100 : pawn c | 4
        bcd: 101 : queen d | 5
        bcd: 110 : rook e | 6
        bcd: 111 : piece (only useful for tests)
        abcd: 0000 : empty square
        config history bit value : A1A2...H8
        @return:
        """
        self.move_historic.append(move)
        # Calcul the config bit value
        config_value = board.dict_to_bit()
        # Update the history
        if config_value in self.config_historic:
            self.config_historic[config_value] += 1
            # TODO moves in game state properly
            # if self.config_historic[config_value] == 3:
            #     self.state = GameState.DRAW
            #     LOGGER.info("Draw with threefold rule")
        else:
            self.config_historic[config_value] = 1
