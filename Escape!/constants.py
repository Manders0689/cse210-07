##FINISH## - We'll all clean this up as we go, then look over everything when we meet Wednesday

from game.casting.color import Color

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

# FONT  --  update font file?
FONT_FILE = "batter/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND  --  update sound files?
BOUNCE_SOUND = "batter/assets/sounds/boing.wav"
WELCOME_SOUND = "batter/assets/sounds/start.wav"
OVER_SOUND = "batter/assets/sounds/over.wav"

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

# LEVELS  -- update file
LEVEL_FILE = "batter/assets/data/level-{:03}.txt"
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
#DEFAULT_LIVES = 3
#MAXIMUM_LIVES = 5

# HUD  --  add timer???
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LEVEL_FORMAT = "LEVEL: {}"
TIMER_FORMAT = "TIME LEFT: {}"
TIMER_GROUP = "timer"
TIME_LIMIT = 6

# BALL  --  delete??
BALL_GROUP = "balls"
BALL_IMAGE = "batter/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# CHARACTER  -- update file
CHARACTER_GROUP = "characters"
CHARACTER_IMAGES = [f"batter/assets/images/{n:03}.png" for n in range(100, 103)]
CHARACTER_WIDTH = 106
CHARACTER_HEIGHT = 28
CHARACTER_RATE = 6
CHARACTER_VELOCITY = 7

# ITEM  --  update files
ITEM_GROUP = "items"
ITEM_IMAGES = {
    "b": [f"batter/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"batter/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"batter/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"batter/assets/images/{i:03}.png" for i in range(40,49)]
}
ITEM_WIDTH = 80
ITEM_HEIGHT = 28
ITEM_DELAY = 0.5
ITEM_RATE = 4
ITEM_MESSAGE = ""

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
