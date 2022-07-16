##FINISH## - Mandy

from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideItemAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        item = cast.get_first_actor(ITEM_GROUP)
        message = item.get_message()
        character = cast.get_first_actor(CHARACTER_GROUP)
        door = cast.get_first_actor(DOOR_GROUP)
        
        character_body = character.get_body()
        item_body = item.get_body()

        if self._physics_service.has_collided(item_body, character_body):
                item.get_message(message)
                # to save that we have found the key
                if item.get_key() == True:
                    door.set_key(True)