from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Door(Actor):

#FINISH!! - Diana

#check to see if key if found
#Save whether key is found or not key_is_found()

#when character collides with door, then: 
# check if key_is_found is true. If yes, open door, go to next level
#   if key_is_found is false, message saying "You must have the key before you can open the door"

    def __init__(self, body, message, key, debug = False):
        """Constructs a new door Character.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        
    def get_message(self):
        """Gets the item's message.
        
        Returns:
            Text representing the item's message.
        """
        return self._message

    def get_key(self):

        return self.get_key
