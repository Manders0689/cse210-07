##FINISH## - Diana
#replace ball with items
#replace racket with character

from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideCharacterAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        item_in_room = cast.get_first_actor(BALL_GROUP)
        character = cast.get_first_actor(CHARACTER_GROUP)
        
        item_in_room_body = item_in_room.get_body()
        character_body = character.get_body()

        if self._physics_service.has_collided(item_in_room_body, character_body):
            item_in_room.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)    