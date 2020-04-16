def get_move(X, Y, j, i):
    moves = [(X + j, Y), (X - j, Y), (X, Y + j), (X, Y - j), (X + j, Y + j), (X - j, Y - j), (X + j, Y - j),  (X - j, Y + j)]
    return moves[i]
