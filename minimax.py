from const import BOARD_LEN
from utils import get_available_move

states = {}
row_scores = {}

def get_score(stones, open_ends, player):
    # print('SCORE -- :stones, open_ends : ', stones, open_ends)
    if stones == 1:
        return stones * open_ends * player
    elif stones == 2:
        return (stones + 2) * open_ends * player
    elif stones == 3:
        return (stones + 5) * open_ends * player
    elif stones == 4:
        if open_ends == 2:
            return 5000 * player
        elif open_ends == 1:
            print('returning 4 stone ')
            return 50 * player
        else:
            return 0
    elif stones >= 5:
        return float('Inf') * player
    
def get_row_score(row):
    row = tuple(row)
    if row not in row_scores:
        # print('row : ', row)
        total_row = 0
        i = 0
        while i < BOARD_LEN + 1:
            if row[i] == 1 or row[i] == 2:
                p = row[i]
                open_ends = 2
                count = 0
                if i == 0 or i == BOARD_LEN or row[i - 1] == (p ^ 3):
                    open_ends -= 1
                while i < BOARD_LEN + 1 and row[i] == p:
                    count += 1
                    i += 1
                if i == BOARD_LEN or row[i] == (p ^ 3):
                    open_ends -= 1
                total_row += get_score(count, open_ends, 1 if p == 2 else -1)
            else:
                i += 1
        row_scores[row] = total_row
        # print('total_row : ', total_row)
        return total_row
    else:
        return row_scores[row]


def get_total_score(matrice):
    total = 0
    # print()
    for i in range(BOARD_LEN):
        total += get_row_score(matrice[i])
        # print('total += : ', total, matrice[i])
    # print('total : ', total)
    return total

def minimax(board, matrice, depth, player):
    if depth == 0:
        return get_total_score(matrice), 0
    # print('in minimax player:', player, board.available_moves)
    # print('matrice : ', matrice)
    if player:
        max_eval = float('-Inf')
        target = (0,0)
        for x, y in board.available_moves:
            m = [row[:] for row in matrice]
            m[y][x] = 2
            _eval, _ = minimax(board, m, depth - 1, False)
            # if depth == 3:
            #     print('MAX DEPTH 3')
            #     print('_eval for max w/ depth 3 and potential target: ', _eval, (x, y))
            if _eval > max_eval:
                max_eval = _eval
                target = (x, y)
        print("returning max eval, target", max_eval, target)
        return max_eval, target
    else:
        min_eval = float('Inf')
        target = (0,0)
        for x, y in board.available_moves:
            m = [row[:] for row in matrice]
            m[y][x] = 1
            _eval, _ = minimax(board, m, depth - 1, True)
            # print('_eval in min: ', _eval)
            # if depth == 2:
            #     print('MIN DEPTH 2')
            #     print('_eval for min: ', _eval)
            #     print()
            if _eval < min_eval:
                min_eval = _eval
                target = (x, y)
        print("returning min eval, target", min_eval, target)
        return min_eval, target