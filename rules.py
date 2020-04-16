from const import BOARD_LEN
from utils import get_move

def capture(moves, X, Y, player):
    captures = []
    for i in range(8):
        x1, y1 = get_move(X, Y, 1, i)
        if (x1, y1, -player) in moves:
            x2, y2 = get_move(X, Y, 2, i)
            if (x2, y2, -player) in moves:
                x3, y3 = get_move(X, Y, 3, i)
                if (x3, y3, player) in moves:
                    captures += [(x1, y1, -player), (x2, y2, -player)]
    return captures
