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

DIRECTIONS = (-10, 10, -1, 1, 11, 9, -9, 11)

WEIGHTS = [
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,  120,  -20,   20,    5,    5,   20,  -20,  120,    0,
    0,  -20,  -40,   -5,   -5,   -5,   -5,  -40,  -20,    0,
    0,   20,   -5,   15,    3,    3,   15,   -5,   20,    0,
    0,    5,   -5,    3,    3,    3,    3,   -5,    5,    0,
    0,    5,   -5,    3,    3,    3,    3,   -5,    5,    0,
    0,   20,   -5,   15,    3,    3,   15,   -5,   20,    0,
    0,  -20,  -40,   -5,   -5,   -5,   -5,  -40,  -20,    0,
    0,  120,  -20,   20,    5,    5,   20,  -20,  120,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0
]

MAXIMUM = sum(map(abs, WEIGHTS))
MINIMUM = -MAXIMUM