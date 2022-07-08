##FINISH## - Katie
#add constants

from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        character = cast.get_first_actor(CHARACTER_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            character.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            character.move_right()  
        elif self._keyboard_service.is_key_down(UP): 
            character.move_up() 
        elif self._keyboard_service.is_key_down(DOWN): 
            character.move_down() 
        else: 
            character.stop_moving()   