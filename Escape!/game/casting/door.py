from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Door(Actor):

    def __init__(self, body, debug = False):
        """Constructs a new door Character.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._message = "You need a key to open the door"
        self._key = False
        
    def get_message(self):
        """Gets the item's message.
        
        Returns:
            Text representing the item's message.
        """
        return self._message

    def get_body(self):
        """Gets the item's body.
    
    Returns:
        An instance of Body.
    """
        return self._body
        
    def get_key(self):

        return self._key
