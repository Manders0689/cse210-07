import time
from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stat including level and 
    remaining time on timer."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._start_time = time.time()
        self._end_time = self._start_time + TIME_LIMIT + 1
        self._time_remaining = TIME_LIMIT + 1

    def set_timer(self):
        """Sets timer to start running. 
        Tracks how much time is remaining."""

        self._time_remaining = int(self._end_time - time.time())

    def get_timer(self):
        "Gets the time remaining"
        
        self.set_timer()

        return self._time_remaining
        
    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._start_time = time.time()
        self._end_time = self._start_time + TIME_LIMIT + 1
        self._time_remaining = TIME_LIMIT + 1
        