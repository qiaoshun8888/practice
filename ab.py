import random


def alphabeta_search(state, game, move, d=4, cutoff_test=None):
    player = state.to_move
    d = (20 / len(game.actions(state))) * 2
    # d = 6 - len(game.actions(state)) / 5  # 3,3,3,4,4,5,5,5,6,6

    def random_action():
        actions = []
        for action in game.actions(state):
            if (action[0] - move[0]) ** 2 + (action[1] - move[1]) ** 2 <= 2:
                actions.append(action)
        return random.choice(actions)

    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = -1
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = 1
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_search starts here:
    # The default test cuts off at depth d or at a terminal state

    def cutoff_test(state, depth):
        return game.terminal_test(state) or depth > d

    def eval_fn(state):
        u = state.utility
        return -u if player == state.to_move else u

    def best(seq):
        best = seq[0]
        best_score = min_value(game.result(state, best), -3, 3, 0)
        for x in seq[1:]:
            x_score = min_value(game.result(state, x), -3, 3, 0)
            if x_score > best_score:
                best, best_score = x, x_score

        print best, best_score, 'result'
        return best

    if len(game.actions(state)) >= 18:
        result = random_action()
    else:
        result = best(game.actions(state))
    return result


# class AlphaBetaSearch():
#     player = 'o'

#     def search(self, state):
#         v = self.max_value(state, -3, +3)
#         return random.choice(state.available_positions())

#     def max_value(self, state, a, b):
#         if state.terminal_test():
#             return state.utility(self.player)
#         v = -3
#         for p in state.available_positions():
#             state.pin(p)
#             v = max(v, self.min_value(state, a, b))
#             state.unpin()
#             if v >= b:
#                 return v
#             a = max(a, v)
#         return v

#     def min_value(self, state, a, b):
#         if state.terminal_test():
#             return state.utility(self.player)
#         v = +3
#         for p in state.available_positions():
#             state.pin(p)
#             v = min(v, self.max_value(state, a, b))
#             state.unpin()
#             if v <= a:
#                 return v
#             a = min(a, v)
#         return v
