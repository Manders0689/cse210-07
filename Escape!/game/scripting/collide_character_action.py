from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideCharacterAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        item_in_room = cast.get_first_actor(ITEM_GROUP)
        door = cast.get_first_actor(DOOR_GROUP)
        character = cast.get_first_actor(CHARACTER_GROUP)
        
        #item_in_room_body = item_in_room.get_body()
        door_body = door.get_body()
        character_body = character.get_body()

        if door.get_key() == False & self._physics_service.has_collided(door_body, character_body): 
            door.get_message()