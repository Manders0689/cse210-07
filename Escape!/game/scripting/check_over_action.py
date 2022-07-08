##FINISH## - Diana

from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        items_in_room = cast.get_actors(ITEM_GROUP)
        if #key_is_found == True and character location == door location:
            stats = cast.get_first_actor(STATS_GROUP)
            stats.next_level()
            callback.on_next(NEXT_LEVEL)