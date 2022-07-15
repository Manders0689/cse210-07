###CLEAN UP AND FINISH## - Alexa
#level
#time

from constants import *
from game.casting.actor import Actor
import time
import datetime

class Stats(Actor):
    """The game stat including level and 
    remaining time on timer."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._timer = TIME_LIMIT

    def set_timer(self, total_seconds):
        while self._timer > 0:
        
            # Timer represents time left on countdown
            timer = datetime.timedelta(seconds = total_seconds)
                
            # Prints the time left on the timer
            # self.set_text(f"Timer: {timer}")
            # print(timer, end="\r")
        
            # Delays the program one second
            time.sleep(1)
        
            # Counts timer down by 1 second
            total_seconds -= 1
        
        return timer
        
    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level
  
    def get_timer(self):
        """Gets the time.

        Returns:
            A number representing the number of seconds left.
        """
        return self._timer
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._timer = TIME_LIMIT
        