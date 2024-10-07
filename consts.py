BUBBLE_GRID_START_ROWS = 5
BUBBLE_GRID_COLS = 15
BUBBLE_RADIUS = 22
BUBBLE_SMALLER_BY = 1
NO_BUBBLE = "EMPTY"
SPACE_BETWEEN_COLS = 3
ROWS_OVERLAP = 1
WINDOW_HEIGHT = 750
WINDOW_WIDTH = BUBBLE_GRID_COLS * (
        BUBBLE_RADIUS * 2 + SPACE_BETWEEN_COLS) + BUBBLE_RADIUS
NUM_OF_LINES_LOSE = 13
NUM_OF_TURNS_TO_ADD_ROW = 5
MIN_CLUSTER_SIZE_TO_POP = 3

RED = (255, 89, 94)
GREEN = (138, 201, 38)
BLUE = (25, 130, 196)
ORANGE = (255, 202, 58)
VIOLET = (106, 76, 147)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (254, 252, 252)
BUBBLE_START_COLORS = [RED, GREEN, BLUE, ORANGE, VIOLET]
BORDER_COLOR = (173, 181, 189)
TURNS_COLOR = (89, 89, 89)
TURNS_TEXT = "Turns left: "
TURNS_FONT_SIZE = 20
TURNS_LOCATION = (10, WINDOW_HEIGHT - TURNS_FONT_SIZE - 10)
FONT_NAME = "Calibri"
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))

ARROW_IMG = "arrow.png"
ARROW_HEIGHT = 100
ARROW_WIDTH = 20
ARROW_X = WINDOW_WIDTH / 2 - (ARROW_WIDTH / 2)
ARROW_Y = WINDOW_HEIGHT * 0.8
ARROW_MIDBOTTOM_X = ARROW_X + ARROW_WIDTH / 2
ARROW_MIDBOTTOM_Y = ARROW_Y + ARROW_HEIGHT

STACK_SIZE = 2
STACK_LOCATION = (ARROW_MIDBOTTOM_X - BUBBLE_RADIUS, ARROW_MIDBOTTOM_Y)

MIN_SAME_COLOR_TO_POP = 3
bubble_colors = BUBBLE_START_COLORS.copy()

RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3

