"""
Alpha Beta Search Algorithm
"""
import random
from datetime import datetime


def alphabeta_search(state, game, move, robot_level=1, progress=None):
    """
    Alpha Beta Search Algorithm
    """
    # record the start time
    _absearch_starttime = datetime.now()
    # set the player
    player = state.to_move

    def max_value(state, alpha, beta, depth):
        """
        Max value
        """
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = -3
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        """
        Min value
        """
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = 3
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def cutoff_test(state, depth):
        """
        Cutoff Test
        1. Test the game whether it is terminal
        2. Test the time is up
        """
        cut = game.terminal_test(state) or depth > d
        time_cut = (
            datetime.now() - _absearch_starttime).seconds > 10
        return cut or time_cut

    def eval_fn(state):
        """
        Actually return the utility value depends who is the player
        """
        u = state.utility
        return -u if player == state.to_move else u

    def best(seq):
        """
        Given the action list
        Return the best action and the time used
        - Shuffle the action list randomly
        - Compare the Min Value of those actions
        - Chose the Max Min Value
        """
        random.shuffle(seq)
        best = seq[0]
        best_score = min_value(
            game.result(state, best), -float('inf'), float('inf'), 0)
        if progress:
            progress['value'] = 0
            progress['maximum'] = len(seq)
        for x in seq[1:]:
            if progress:
                progress['value'] += 1
            x_score = min_value(
                game.result(state, x), -float('inf'), float('inf'), 0)
            if x_score > best_score:
                best, best_score = x, x_score
        progress['value'] = 0
        return best

    def random_action():
        """
        Randomly choose a action, only called when robot is the first player
        """
        actions = game.actions(state)
        action = random.choice(actions)
        while action[1] in [0, game.width - 1] or action[0] in [0, game.height - 1]:
            # avoid choose action near edges
            action = random.choice(actions)
        return action

    if not move:
        # if it is the first move of the game
        # return a random action
        return random_action(), 0
    else:
        d = robot_level
        best = best(game.actions(state))
        time_used = (datetime.now() - _absearch_starttime).seconds
        return best, time_used
