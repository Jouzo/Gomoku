from const import BOARD_LEN

def get_diagonal(matrice, i):
    ret = [[0 for _ in range(BOARD_LEN)] for _ in range(4)]
    for x in range(BOARD_LEN - i):
        ret[0][i + x] = matrice[x + i][x]
        ret[1][i + x] = matrice[x][x + i]
        ret[2][i + x] = matrice[(BOARD_LEN - 1) - x - 1][(BOARD_LEN - 1) - x]
        ret[3][i + x] = matrice[(BOARD_LEN - 1) - x][(BOARD_LEN - 1) - x - 1]
    return ret


def get_move(X, Y, j, i):
    moves = [(X - j, Y), (X + j, Y), (X - j, Y - j), (X + j, Y + j), (X + j, Y - j), (X - j, Y + j), (X, Y + j), (X, Y - j)]
    return moves[i]

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

# def get_hash_key(matrice):
#     return ''.join([''.join([chr(x + 65) for x in row]) for row in matrice])
