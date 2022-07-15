###CLEAN UP AND FINISH## - Alexa
#level
#time

from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stat including level."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._timer = TIME_LIMIT

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level
  
    def get_timer(self):
        """Gets the time.

        Returns:
            A number representing the time.
        """
        return self._timer
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._timer = TIME_LIMIT
        