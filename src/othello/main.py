from constants import *


def cells():
    return [index
            for index in range(11, 89)
            if 1 <= (index % 10) <= 8]


def initialization():
    board = [FRINGE] * 100

    for index in cells():
        board[index] = VACANT

    board[44], board[45] = WHITE, BLACK
    board[54], board[55] = BLACK, WHITE

    return board


def illustrate(board):
    flush = f'  {" ".join(map(str, range(1, 9)))}\n'

    for row in range(1, 9):
        start, stop = 10 * row + 1, 10 * row + 9
        flush += f'{row} {" ".join(board[start:stop])}\n'

    print(flush)


def on_the_board(move):
    return isinstance(move, int) and move in cells()


def opponent(player):
    return WHITE if player is BLACK else BLACK


def batch(square, player, board, direction):
    point = square + direction
    if board[point] == player:
        return None

    foe = opponent(player)

    while board[point] == foe:
        point += direction

    return None if board[point] in (FRINGE, VACANT) else point


def is_legal(move, player, board):
    def seek(direction):
        return batch(move, player, board, direction)
    return board[move] == VACANT and any(map(seek, DIRECTIONS))


def progress(move, player, board):
    board[move] = player
    for direction in DIRECTIONS:
        invert_discs(move, player, board, direction)
    return board


def invert_discs(move, player, board, direction):
    point = batch(move, player, board, direction)
    if point is None:
        return

    square = move + direction
    while square != point:
        board[square] = player
        square += direction


def legal_moves(player, board):
    return [square
            for square in cells()
            if is_legal(square, player, board)]


def any_legal_moves(player, board):
    return any(is_legal(square, player, board)
               for square in cells())


def score(player, board):
    foe = opponent(player)
    player, computer = 0, 0

    for square in cells():
        piece = board[square]

        if piece == player:
            player += 1
        elif piece == foe:
            computer += 1

    return player - computer


def decide(player, board):
    difference = score(player, board)

    if difference < 0:
        return MINIMUM
    elif difference > 0:
        return MAXIMUM
    else:
        return difference


def minimax(player, board, alpha, beta, depth, evaluate):
    if depth == 0:
        return evaluate(player, board), None

    def value(board, alpha, beta):
        return -minimax(opponent(player), board, -beta, -alpha, depth - 1, evaluate)[0]

    moves = legal_moves(player, board)
    if not moves:
        if not any_legal_moves(opponent(player), board):
            return decide(player, board), None
        return value(board, alpha, beta), None

    ultimate = moves[0]
    for move in moves:
        if alpha >= beta:
            break

        cost = value(progress(move, player, list(board)), alpha, beta)

        if cost > alpha:
            alpha = cost
            ultimate = move

    return alpha, ultimate


def search(depth, evaluate):
    def strategy(player, board):
        return minimax(player, board, MINIMUM, MAXIMUM, depth, evaluate)[1]
    return strategy


def verify(move, player, board):
    return on_the_board(move) and is_legal(move, player, board)


def human(player, board):
    illustrate(board)

    while True:
        move = int(input(': '))

        if verify(move, player, board):
            return move
        else:
            print(f'{move} is Illegal')


def play(black, white):
    board = initialization()
    player = BLACK

    def strategy(who):
        return black if who == BLACK else white

    while player is not None:
        move = fetch(strategy(player), player, board)
        progress(move, player, board)
        player = then(board, player)

    return board, score(BLACK, board)


def fetch(strategy, player, board):
    clone = list(board)
    move = strategy(player, clone)

    if not on_the_board(move) or not is_legal(move, player, board):
        raise

    return move


def then(board, previous):
    foe = opponent(previous)

    if any_legal_moves(foe, board):
        return foe
    elif any_legal_moves(previous, board):
        return previous
    else:
        return None
