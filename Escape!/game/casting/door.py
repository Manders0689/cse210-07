from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Door(Actor):

    def __init__(self, body, image, debug = False):
        """Constructs a new door Character.
        
        Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._key = False
        self._image = image

    def get_body(self):
        """Gets the item's body.
    
    Returns:
        An instance of Body.
    """
        return self._body
        
    def get_key(self):
        """Gets if the item has the key or not.

        Returns:
            Boolean representing if an item has the key.
        """
        return self._key

    def set_key(self, key):
        """Sets if the item has the key or not.

        Args: 
            key: true or false if the key has been found
        """
        self._key = key

    def get_image(self):
        """Gets the door image.

        Returns:
            door image path.
        """
        return self._image
