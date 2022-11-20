"""
Empty Move, to initialize the game history
"""
from src.domain.classes.const.column import Column
from src.domain.classes.square import Square
from src.domain.events.moves.move import Move


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
