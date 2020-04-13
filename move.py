from const import BOARD_LEN
from score import get_total_score
from rules import capture
from utils import get_move

""" sort available moves by their static analysis score.
    return only the 15 first ones to limit branching."""

def sort_moves(matrice, moves, player):
    ret = []
    for x, y in moves:
        matrice[y][x] = player
        c = capture(matrice, x, y, player)
        if len(c):
            for X, Y, _ in c:
                matrice[Y][X] = 0
        score = get_total_score(matrice)
        ret.append((score, (x,y)))
        matrice[y][x] = 0
        if len(c):
            for X, Y, p in c:
                matrice[Y][X] = p
    
    ret.sort(key=lambda x: x[0], reverse=True)
    return [x[1] for x in ret][:15]


def get_available_move(matrice):
    moves = []
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            if matrice[i][j]:
                for k in range(8):
                    x, y = get_move(j, i, 1, k)
                    if 0 <= x < BOARD_LEN and 0 <= y < BOARD_LEN and not matrice[y][x]:
                        moves.append((x, y))
    return moves
