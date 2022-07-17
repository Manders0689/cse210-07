from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
# for adding dialogue
from game.casting.label import Label
from game.casting.point import Point
from game.casting.text import Text 


class CollideItemAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        items = cast.get_actors(ITEM_GROUP)
        character = cast.get_first_actor(CHARACTER_GROUP)
        character_body = character.get_body()
        door = cast.get_first_actor(DOOR_GROUP)

        for item in items:
            item_body = item.get_body()

            if self._physics_service.has_collided(item_body, character_body):
                    
                    def _add_dialog(self, cast, message):
                        cast.clear_actors(DIALOG_GROUP)
                        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
                        position = Point(CENTER_X, CENTER_Y)
                        label = Label(text, position)
                        cast.add_actor(DIALOG_GROUP, label)

                    _add_dialog(self, cast, item.get_message())

                    # save that we found the key
                    if item.get_key() == 'True':
                        door.set_key(True)        