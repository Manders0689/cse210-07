from constants import *
from game.scripting.action import Action


class DrawItemsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        items = cast.get_actors(ITEM_GROUP)
        
        for item in items:
            body = item.get_body()

            if item.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = item.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)