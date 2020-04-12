from const import BOARD_LEN
from utils import get_move

def capture(matrice, player, X, Y):
    captures = []
    for i in range(8):
        x1, y1 = get_move(X, Y, 1, i)
        if 0 <= x1 < BOARD_LEN and 0 <= y1 < BOARD_LEN and matrice[y1][x1] == -player:
            x2, y2 = get_move(X, Y, 2, i)
            if 0 <= x2 < BOARD_LEN and 0 <= y2 < BOARD_LEN and matrice[y2][x2] == -player:
                x3, y3 = get_move(X, Y, 3, i)
                if 0 <= x3 < BOARD_LEN and 0 <= y3 < BOARD_LEN and matrice[y3][x3] == player:
                    captures += [(x1, y1, -player), (x2, y2, -player)]
    return captures