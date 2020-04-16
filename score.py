from const import BOARD_LEN, CAPTURE_SCORE
from utils import get_move

counts = []
which = ''

def get_score(stones, open_ends, player, playing):
    if open_ends == 0 and stones < 5:
        return 0
    if stones == 1:
        return stones * open_ends / 2
    elif stones == 2:
        return stones * open_ends + (open_ends - 1)
    elif stones == 3:
        if open_ends == 2:
            if player is playing:
                return 1000
            else:
                return 50
        else:
            if player is playing:
                return 10
            else:
                return 5
    elif stones == 4:
        if open_ends == 2:
            if player is playing:
                return 1000000
            else:
                return 50000
        elif open_ends == 1:
            if player is playing:
                return 1000000
            else:
                return 50
    elif stones >= 5:
        return 3000000
    

def get_half(x, y, player, moves, i, _set, val):
    count = 0
    while (x, y, player) in moves and (x, y) not in _set:
        _set.add((x, y, player))
        count += 1
        counts.append((x, y, player))
        x, y = get_move(x, y, val, i)
        if (x, y, -player) in moves:
            break
        elif (x, y, player) in moves:
            continue
        else:
            x, y = get_move(x, y, val, i)
    return count, int((x, y, -player) in moves)

def get_row(X, Y, player, state, i, _set):
    _set.add((X, Y, player))
    global counts
    counts = [(X, Y, player)]
    count = 1
    open_ends = 2

    c, o = get_half(*get_move(X, Y, 1, i), player, state.moves, i, _set, 1)
    count += c
    open_ends -= o
    c, o = get_half(*get_move(X, Y, 1, i + 1), player, state.moves, i + 1, _set, 1)
    count += c
    open_ends -= o
    total = get_score(count, open_ends, player, -state.player)
    
    # print('move : ', X, Y, player)
    # print('counts : ', counts)
    # print('total : ', total)
    
    return total * player

def get_total_score(state):
    total = 0
    global which

    rows = set()
    cols = set()
    diag1 = set()
    diag2 = set()
    for move in state.moves:
        which = ''
        if move not in rows:
            total += get_row(*move, state, 0, rows)
            # print('total after rows : ', total)
        if move not in cols:
            total += get_row(*move, state, 2, cols)
            # print('total after cols : ', total)
        if move not in diag1:
            which = 'diag1'
            total += get_row(*move, state, 4, diag1)
        if move not in diag2:
            total += get_row(*move, state, 6, diag2)
    # print('state.moves', state.moves)
    # print('total : ', total * -1)
    return total + (CAPTURE_SCORE[str(state.captures[str(state.player)])] - CAPTURE_SCORE[str(state.captures[str(-state.player)])])
