from const import BOARD_LEN
from score import get_total_score
from state import State


""" sort available moves by their static analysis score.
    return only the 15 first ones to limit branching."""

def sort_moves(state, player, depth):
    ret = []
    for x, y in state.available_moves:
        new_state = State(state, player, depth)
        new_state.add_move(x, y, player)
        score = get_total_score(new_state)
        ret.append((score, (x,y)))
    ret.sort(key=lambda x: x[0], reverse=False)
    # print(ret)
    return [x[1] for x in ret][:10]

def minimax(state, depth, player, alpha, beta):
    if depth == 0:
        return get_total_score(state) * player, 0
    
    max_eval = float('-Inf')
    target = (0,0)
    
    if depth >= 3:
        moves = sort_moves(state, state.player, depth)
    else:
        moves = state.available_moves
    for x, y in moves:
        new_state = State(state, player, depth - 1)
        new_state.add_move(x, y, player)
        _eval = -minimax(new_state, depth - 1, -player, -alpha, -beta)[0]
        if _eval > max_eval:
            max_eval = _eval
            target = (x, y)
        alpha = max(alpha, _eval)
        if alpha >= beta:
            break
    return max_eval, target