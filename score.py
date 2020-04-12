from const import BOARD_LEN

row_scores = {}

def get_score(stones, open_ends, player):
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
            return 50 * player
        else:
            return 0
    elif stones >= 5:
        return float('Inf') * player
    
def get_row_score(row):
    row = tuple(row)
    if row not in row_scores:
        total_row = 0
        i = 0
        while i < BOARD_LEN:
            if row[i] == 1 or row[i] == -1:
                player = row[i]
                open_ends = 2
                count = 0
                if i == 0 or i == BOARD_LEN - 1 or row[i - 1] == -player:
                    open_ends -= 1
                while i < BOARD_LEN and row[i] == player:
                    count += 1
                    i += 1
                if i == BOARD_LEN or row[i] == -player:
                    open_ends -= 1
                total_row += get_score(count, open_ends, -player)
            else:
                i += 1
        row_scores[row] = total_row
        return total_row
    else:
        return row_scores[row]


def get_total_score(matrice):
    total = 0
    for i in range(BOARD_LEN):
        total += get_row_score(matrice[i])
        total += get_row_score([x[i] for x in matrice])
        # for x in get_diagonal(matrice, i):
        #     total += get_row_score(x)
    return total
