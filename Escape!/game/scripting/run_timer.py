from constants import *
from game.scripting.action import Action

class RunTimer(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        """Checks if no time is left on the timer
        and sets game over if time is out."""

        stats = cast.get_first_actor(STATS_GROUP)
        timer = stats.get_timer()

        if timer < 0:
            callback.on_next(GAME_OVER)
            print(time.time())

