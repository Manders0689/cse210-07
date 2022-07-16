from constants import *
from game.scripting.action import Action


class DrawDoorAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        door = cast.get_first_actor(DOOR_GROUP)
        body = door.get_body()

        if door.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = door.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)