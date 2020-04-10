from const import BOARD_LEN

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
