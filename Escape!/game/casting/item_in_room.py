from game.casting.actor import Actor

class Item(Actor):
    """A solid object that can be interacted with."""

    def __init__(self, body, message, image, has_key, debug = False):
        """Constructs a new Item.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged.
            message: Message to display. 
        """
        super().__init__(debug)
        self._body = body
        self._message = message
        self._image = image
        self._has_key = has_key

    def get_body(self):
        """Gets the item's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_text(self):
        """Gets the item's message.
        
        Returns:
            Text representing the item's message.
        """
        return self._message
    
    def get_image(self):
        """Gets the item's image.
        
        Returns:
            string representing the item's image path.
        """
        return self._image
    
    def get_key(self):
        """Gets boolean if the item has the key.
        
        Returns:
            Boolean representing if the item has the key.
        """
        return self._has_key