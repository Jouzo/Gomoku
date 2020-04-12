from const import BOARD_LEN
from move import get_available_move, sort_moves
from score import get_total_score
from rules import capture

def minimax(board, matrice, depth, player, alpha, beta):
    if depth == 0:
        return get_total_score(matrice) * -1, 0
    max_eval = float('-Inf')
    target = (0,0)
    
    if depth == 3:
        moves = sort_moves(matrice, board.available_moves, player)
    else:
        moves = board.available_moves

    for x, y in moves:
        m = [row[:] for row in matrice]
        m[y][x] = player
        
        c = capture(m, player, x, y)
        if len(c):
            for X, Y, _ in c:
                m[Y][X] = 0

        _eval = -minimax(board, m, depth - 1, -player, -alpha, -beta)[0]
       
        if _eval > max_eval:
            max_eval = _eval
            target = (x, y)
        alpha = max(alpha, _eval)
        if alpha >= beta:
            break
    return max_eval, target