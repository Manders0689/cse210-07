##FINISH## - Mandy

from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideItemAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        #ball = cast.get_first_actor(BALL_GROUP)
        items = cast.get_actors(ITEM_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        message = cast.get_message(MESSAGE_GROUP)
        
        for item in items:
            #ball_body = ball.get_body()
            item_body = item.get_body()

            if self._physics_service.has_collided(item_body):
                #ball.bounce_y()
                #sound = Sound(BOUNCE_SOUND)
                #self._audio_service.play_sound(sound)
                #points = brick.get_points()
                #stats.add_points(points)
                #cast.remove_actor(BRICK_GROUP, brick)
                stats.get_message(message) ##Is this in stats?