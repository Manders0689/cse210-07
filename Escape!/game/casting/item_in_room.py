#based off of brick
# May need work#
from game.casting.actor import Actor


class Item(Actor):
    """A solid object that can be interacted with."""

    def __init__(self, body, animation, message, debug = False):
        """Constructs a new Item.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged.
            message: Message to display. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._message = message
        
    def get_animation(self):
        """Gets the item's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the item's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_message(self):
        """Gets the item's message.
        
        Returns:
            Text representing the item's message.
        """
        return self._message
    