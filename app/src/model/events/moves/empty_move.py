"""
Empty Move, to initialize the game history
"""
from app.src.model.events.moves.move import Move
from app.src.model.game.square import Square
from app.src.model.miscenaleous.column import Column


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
