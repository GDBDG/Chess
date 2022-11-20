"""
Empty Move, to initialize the game history
"""
from src.CHESS.domain.classes.const.column import Column
from src.CHESS.domain.classes.square import Square
from src.CHESS.domain.events.moves.move import Move


class EmptyMove(Move):
    """
    Empty moves classes
    """

    def __init__(
        self,
    ):
        """
        Constructor
        """
        super().__init__(Square(Column.D, 4), Square(Column.D, 4))
