from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveCharacterAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        character = cast.get_first_actor(CHARACTER_GROUP)
        body = character.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        
        position = position.add(velocity)

        if x < 0 and y < 60:
            position = Point(0, 60)
        elif x > (SCREEN_WIDTH - CHARACTER_WIDTH) and y < 60:
            position = Point(SCREEN_WIDTH - CHARACTER_WIDTH, 60)
        elif x < 0 and y > (SCREEN_HEIGHT - CHARACTER_HEIGHT):
            position = Point(0, SCREEN_HEIGHT - CHARACTER_HEIGHT)  
        elif x > (SCREEN_WIDTH - CHARACTER_WIDTH) and y > (SCREEN_HEIGHT - CHARACTER_HEIGHT):
            position = Point(SCREEN_WIDTH - CHARACTER_WIDTH, SCREEN_HEIGHT - CHARACTER_HEIGHT)   
        else:
            position = Point(position.get_x(), position.get_y())

        body.set_position(position)
        