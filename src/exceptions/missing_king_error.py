"""
Error if there is no king in the game
"""


class MissingKingError(Exception):
    """
    Error classes
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.message = "King missing"

    def __repr__(self):
        return self.message
