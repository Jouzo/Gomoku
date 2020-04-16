from move import get_available_move
from rules import capture

class State():
    def __init__(self, state, player, depth):
        self.available_moves = set.copy(state.available_moves)
        self.captures = {'1' : state.captures['1'], '-1': state.captures['-1'] }
        self.moves = set.copy(state.moves)
        self.player = player
        self.depth = depth
    
    def add_move(self, x, y, player):
        # print('adding move (x, y, player)', (x, y, player), 'depth:', self.depth)
        self.moves.add((x, y, player))
        self.available_moves.update(get_available_move(self.moves, x, y))
        self.available_moves.discard((x, y))
        captures = capture(self.moves, x, y, player)
        if len(captures):
            for x, y, p in captures:
                self.moves.remove((x, y, p))
                self.available_moves.add((x, y))
                self.captures[str(player)] += 1
