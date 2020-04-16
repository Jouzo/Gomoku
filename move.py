from const import BOARD_LEN
from score import get_total_score
from rules import capture
from utils import get_move

def get_available_move(moves, X, Y):
    ret = []
    for i in range(8):
        x, y = get_move(X, Y, 1, i)
        if 0 <= x < BOARD_LEN and 0 <= y < BOARD_LEN \
            and (x, y, 1) not in moves and (x, y, -1) not in moves:
            ret.append((x, y))
    return ret
