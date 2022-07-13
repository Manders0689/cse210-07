### ALEXA


from constants import *
from game.casting.actor import Actor
import datetime
import time


class Timer(Actor):

    def __init__(self):
        self.seconds_left = ""
        self.count_down(TIME_LIMIT)


    def count_down(self, total_seconds):
        """
        """

        # While loop that checks if total_seconds reaches zero
        # If not zero, decrement total time by one second
        self._time = TIME_LIMIT
        while self._time > 0:
        
            # Timer represents time left on countdown
            timer = datetime.timedelta(seconds = total_seconds)
                
            # Prints the time left on the timer
            self.set_text(f"Timer: {timer}")
            # print(timer, end="\r")
        
            # Delays the program one second
            time.sleep(1)
        
            # Counts timer down by 1 second
            total_seconds -= 1