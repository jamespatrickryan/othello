DIMENSION = 160
BOARD = 8

GREEN = 'green'
PLAYER = 'black'
COMPUTER = 'white'
YELLOW = 'yellow'

FRINGE = '?'
VACANT = '.'
BLACK = '@'
WHITE = 'o'

UP = -10
DOWN = 10
LEFT = -1
RIGHT = 1
UP_LEFT = -11
DOWN_LEFT = 9
UP_RIGHT = -9
DOWN_RIGHT = 11

DIRECTIONS = (
    UP,
    DOWN,
    LEFT,
    RIGHT,
    UP_LEFT,
    DOWN_LEFT,
    UP_RIGHT,
    DOWN_RIGHT
)

WEIGHTS = [
    0,   0,   0,  0,  0,  0,  0,   0,   0, 0,
    0, 120, -20, 20,  5,  5, 20, -20, 120, 0,
    0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
    0,  20,  -5, 15,  3,  3, 15,  -5,  20, 0,
    0,   5,  -5,  3,  3,  3,  3,  -5,   5, 0,
    0,   5,  -5,  3,  3,  3,  3,  -5,   5, 0,
    0,  20,  -5, 15,  3,  3, 15,  -5,  20, 0,
    0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
    0, 120, -20, 20,  5,  5, 20, -20, 120, 0,
    0,   0,   0,  0,  0,  0,  0,   0,   0, 0
]

MAXIMUM = sum(map(abs, WEIGHTS))
MINIMUM = -MAXIMUM
