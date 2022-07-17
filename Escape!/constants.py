##FINISH## - We'll all clean this up as we go, then look over everything when we meet Wednesday

from game.casting.color import Color
import time

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Escape!"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT  
FONT_FILE = "Escape!/assets/fonts/SpecialElite-Regular.ttf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND  
WELCOME_SOUND = "Escape!/assets/sounds/start.wav"
OVER_SOUND = "Escape!/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4
YOU_WIN = 5

# LEVELS 
LEVEL_FILE = "Escape!/assets/data/level-{:03}.csv"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
MESSAGE_GROUP = "message"
TIME_LIMIT = 60

# # # # # HARDCODED TIMER
# # # # START_TIME = time.time()
# # # # TIME_LIMIT = 15
# # # # END_TIME = START_TIME + TIME_LIMIT

# HUD 
HUD_MARGIN = 15
LEVEL_GROUP = "level"
TIMER_GROUP = "timer"
LEVEL_FORMAT = "LEVEL: {}"
TIMER_FORMAT = "TIME LEFT: {}"

# DOOR
DOOR_GROUP = "door"
DOOR_IMAGE = "Escape!/assets/images/door.png"
DOOR_WIDTH = 100
DOOR_HEIGHT = 160

# CHARACTER  
CHARACTER_GROUP = "characters"
CHARACTER_IMAGES = [f"Escape!/assets/images/{n:01}.png" for n in range(1, 3)]
CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 70
CHARACTER_RATE = 10
CHARACTER_VELOCITY = 7

# ITEM -- deleted item images
ITEM_GROUP = "items"
ITEM_WIDTH = 80
ITEM_HEIGHT = 80
ITEM_DELAY = 0.5
ITEM_RATE = 4
ITEM_MESSAGE = ""

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO START"
WAS_GOOD_GAME = "GAME OVER"
WIN = "CONGRATULATIONS! YOU WIN!"