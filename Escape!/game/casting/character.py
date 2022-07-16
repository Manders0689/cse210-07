from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Character(Actor):
    """A character to move around the room."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Character.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the character's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the character's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the character using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_left(self):
        """Steers the character to the left."""
        velocity = Point(-CHARACTER_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def move_right(self):
        """Steers the character to the right."""
        velocity = Point(CHARACTER_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def move_up(self):
        """Steers the character to the left."""
        velocity = Point(0, -CHARACTER_VELOCITY)
        self._body.set_velocity(velocity)
        
    def move_down(self):
        """Steers the character to the right."""
        velocity = Point(0, CHARACTER_VELOCITY)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the character from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)