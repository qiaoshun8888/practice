import copy


class State():
    board = None
    to_move = None
    moves = None
    utility = None

    def __init__(self, game):
        self.board = {}
        for i in range(game.height):
            for j in range(game.width):
                self.board[(i, j)] = None

        self.to_move = 'x'
        self.moves = self.board.keys()
        self.utility = 0


class Game():
    count = 0
    width = 5
    height = 4
    next = 'x'
    players = ('o', 'x')
    robot = None
    last = None
    directions = (((0, 1), (0, -1)),
                 ((1, 1), (-1, -1)),
                 ((1, 0), (-1, 0)),
                 ((1, -1), (-1, 1)))

    def __init__(self, width=5, height=4):
        self.width = width
        self.height = height
        self.robot = 'o'

    def actions(self, state):
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state  # no effect
        _state = copy.deepcopy(state)
        _state.board[move] = state.to_move
        _state.to_move = 'x' if state.to_move == 'o' else 'o'
        _state.moves.remove(move)
        _state.utility = self.utility(_state, state.to_move)
        return _state

    def utility(self, state, player):
        u = self.con('x', state) - self.con('o', state)
        return u if player == 'x' else -u

    def terminal_test(self, state):
        if not self.actions(state):
            return True
        if self.con('x', state) >= 4 or self.con('o', state) >= 4:
            return True
        return False

    # def unpin(self):
    #     if not state[self.last[0]][self.last[1]] == self.next:
    #         state[self.last[0]][self.last[1]] = None
    #     self.count -= 1
    #     self.next = 'x' if self.next == 'o' else 'o'

    def subcon(self, ox, block, direction, state):
        '''
        count only one diriection
        '''
        c = 1
        for d in direction:
            (tmp_i, tmp_j) = block
            tmp_i += d[0]
            tmp_j += d[1]
            while tmp_i <= self.height - 1 and tmp_j <= self.width - 1 and tmp_i >= 0 and tmp_j >= 0:
                if not state.board[(tmp_i, tmp_j)] == ox:
                    break
                else:
                    c += 1
                    tmp_i += d[0]
                    tmp_j += d[1]
        return c

    def con(self, ox, state):
        '''
        count
        '''
        max_con = 1
        for k, v in state.board.items():
            if v == ox:
                for direction in self.directions:
                    subcon = self.subcon(ox, k, direction, state)
                    if subcon >= 4:
                        return 4
                    elif subcon > max_con:
                        max_con = subcon
        return max_con
