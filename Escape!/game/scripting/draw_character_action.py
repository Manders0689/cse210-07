##MAY NEED TO GET RID OF RECTANGLE OR PURPLE COLOR##

from constants import *
from game.scripting.action import Action


class DrawCharacterAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        character = cast.get_first_actor(CHARACTER_GROUP)
        body = character.get_body()

        if character.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = character.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)