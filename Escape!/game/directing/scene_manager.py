###CLEAN UP AND FINISH### - Katie
###Make changes to fix game###

import csv
from constants import *
from game.casting.animation import Animation
from game.casting.body import Body
from game.casting.item_in_room import Item
from game.casting.door import Door
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.character import Character
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_item_action import CollideItemAction
from game.scripting.collide_character_action import CollideCharacterAction
from game.scripting.control_character_action import ControlCharacterAction
from game.scripting.draw_items_action import DrawItemsAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_character_action import DrawCharacterAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_character_action import MoveCharacterAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    CHECK_OVER_ACTION = CheckOverAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_ITEM_ACTION = CollideItemAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_CHARACTER_ACTION = CollideCharacterAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_CHARACTER_ACTION = ControlCharacterAction(KEYBOARD_SERVICE)
    DRAW_ITEMS_ACTION = DrawItemsAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_CHARACTER_ACTION= DrawCharacterAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_CHARACTER_ACTION = MoveCharacterAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_door(cast)
        self._add_items(cast)
        self._add_character(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_items(cast)
        self._add_character(cast)
        self._add_door(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_items(cast)
        self._add_door(cast)
        self._add_character(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_CHARACTER_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)
        # check dialogue?

    def _prepare_game_over(self, cast, script):
        self._add_items(cast)
        self._add_door(cast)
        self._add_character(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    def _add_items(self, cast):
        cast.clear_actors(ITEM_GROUP)
        
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True, delimiter=",")
            # skip header line
            next(reader)
            #create dictionary
            main_dict = {n[0]: [int(n[1]), int(n[2]), n[3], n[4], n[5]] for n in reader}         
            
        for item in main_dict.items():
            key = item[0]
            value = item[1]
            x = value[0]
            y = value[1]
            message = value[2]
            has_key = value[3]
            image = value[4]
            position = Point(x, y)
            size = Point(ITEM_WIDTH, ITEM_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            item = Item(body, message, image, has_key)
            cast.add_actor(ITEM_GROUP, item)
        
    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_character(self, cast):
        cast.clear_actors(CHARACTER_GROUP)
        x = CENTER_X - CHARACTER_WIDTH / 2
        y = SCREEN_HEIGHT - CHARACTER_HEIGHT
        position = Point(x, y)
        size = Point(CHARACTER_WIDTH, CHARACTER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(CHARACTER_IMAGES, CHARACTER_RATE)
        character = Character(body, animation)
        cast.add_actor(CHARACTER_GROUP, character)

    def _add_door(self, cast):
        cast.clear_actors(DOOR_GROUP)
        x = CENTER_X - (DOOR_WIDTH / 2)
        y = SCREEN_HEIGHT - DOOR_HEIGHT
        position = Point(x, y)
        size = Point(DOOR_WIDTH, DOOR_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        door = Door(body)
        cast.add_actor(DOOR_GROUP, door)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_ITEMS_ACTION)
        script.add_action(OUTPUT, self.DRAW_CHARACTER_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_CHARACTER_ACTION)
        script.add_action(UPDATE, self.COLLIDE_ITEM_ACTION)
        script.add_action(UPDATE, self.COLLIDE_CHARACTER_ACTION)
        script.add_action(UPDATE, self.MOVE_CHARACTER_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)