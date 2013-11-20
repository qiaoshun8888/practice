import random
from datetime import datetime


def alphabeta_search(state, game, move, robot_level=1, progress=None):
    _absearch_starttime = datetime.now()
    player = state.to_move

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

    def cutoff_test(state, depth):
        cut = game.terminal_test(state) or depth > d
        time_cut = (datetime.now() - _absearch_starttime).seconds > 10
        return cut or time_cut

    def eval_fn(state):
        u = state.utility
        return -u if player == state.to_move else u

    def best(seq):
        best = seq[0]
        best_score = min_value(game.result(state, best), -3, 3, 0)
        if progress:
            progress['value'] = 0
            progress['maximum'] = len(seq)
        for x in seq[1:]:
            if progress:
                progress['value'] += 1
            x_score = min_value(game.result(state, x), -3, 3, 0)
            if x_score > best_score:
                best, best_score = x, x_score
        progress['value'] = 0
        return best

    def random_action():
        actions = game.actions(state)
        action = random.choice(actions)
        print[0, game.width - 1], [0, game.height - 1]
        while action[1] in [0, game.width - 1] or action[0] in [0, game.height - 1]:
            action = random.choice(actions)
        return action

    # if len(game.actions(state)) >= 18:
    #     result = random_action()
    # else:
    if not move:
        return random_action()
    else:
        d = (20 / len(game.actions(state))) * robot_level
        return best(game.actions(state))
