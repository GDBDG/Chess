"""
Constants for game state (running, white win, equal, black win)
"""
from enum import Enum


class GameState(Enum):
    """
    Game state constants enum
    """

    RUNNING = "running"
    WHITE_WIN = "+/-"
    BLACK_WIN = "-/+"
    DRAW = "-/-"
