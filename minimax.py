# calculate execution time
#
# from time import perf_counter
# t_start = perf_counter()
# t_end = perf_counter() - t_start
# print('Duration:' + ' %.4f seconds' % (t_end))

states = {}

def get_hash_key(matrice):
    return ''.join([''.join([chr(x + 65) for x in row]) for row in matrice])

def minimax(matrice):
    _hash = get_hash_key(matrice)
    states[_hash] = matrice
    return _hash