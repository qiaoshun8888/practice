"""
Models of Game and Gamestate(State)
"""
import copy


class State():

    """
    State encapsulates:
        game    - current game within
        board   - a dict for board state
        to_move - who should play next
        moves   - available moves
        utility - utility of current state
        initial_to_move - who should play first after restart the state
    """
    board = None
    to_move = None
    moves = None
    utility = None
    initial_to_move = None
    game = None

    def __init__(self, game, to_move='o'):
        self.game = game
        self.initial_to_move = to_move
        self.start_new()

    def start_new(self):
        """
        Start a new state, empty all cells, and reset to_move, moves and utility
        """
        self.to_move = self.initial_to_move
        self.board = {}
        for i in range(self.game.height):
            for j in range(self.game.width):
                self.board[(i, j)] = None
        self.moves = self.board.keys()
        self.utility = 0

    def display(self):
        """
        Display the state as a matrix
        Only used in debug mode
        """
        for i in range(self.game.height):
            print '\n'
            for j in range(self.game.width):
                print self.board[(i, j)],
        print '\n--------\n'


class Game():

    """
    Game encapsulates:
        width   - board width, init with 5
        height  - board height, init with 4
        robot   - robot's symbol, init with x
    """

    def __init__(self, width=5, height=4):
        self.width = width
        self.height = height
        self.robot = 'x'
        self.set_ox_list()

    def actions(self, state):
        """
        Given state, return available actions
        In this game, the available actions is the available moves of state
        """
        return state.moves

    def result(self, state, move):
        """
        Given state and move, return state after this move
        Will check if the move is available
        Will set the to_move, moves and utility for the result state instance
        Will set the last for the game instance
        """
        if move not in state.moves:
            return state  # no effect
        _state = copy.deepcopy(state)
        _state.board[move] = state.to_move
        _state.to_move = 'x' if state.to_move == 'o' else 'o'
        _state.moves.remove(move)
        _state.utility = self.utility(_state, state.to_move)
        return _state

    def utility(self, state, player):
        """
        Given state and player(player's symbol), return utility value
        Calculate the utility
        """

        u = self.eval(state)
        return u if player == 'x' else -u

    def terminal_test(self, state):
        """
        Given state, return if the game is end
        - no more available actions
        - someone wins
        """
        if not self.actions(state):
            return True
        if self.win(state):
            return True
        return False

    def terminal_result(self, state):
        """
        Given state, return the terminal state description
        Should only be called when terminal_test is True
        """
        if self.win(state, 'x') and not self.win(state, 'o'):
            return 'X!'
        elif self.win(state, 'o') and not self.win(state, 'x'):
            return 'O!'
        elif not self.actions(state):
            return 'Draw!'
        else:
            return 'Not over'

    def set_ox_list(self):
        """
        Set a list of all row, column, diag blocks
        For the evaluation function to check
        """
        hdic = {}
        vdic = {}
        ldic = {}
        rdic = {}
        for i in range(self.height):
            for j in range(self.width):
                if i in hdic:
                    hdic[i].append((i, j))
                else:
                    hdic[i] = [(i, j)]

                if j in vdic:
                    vdic[j].append((i, j))
                else:
                    vdic[j] = [(i, j)]

                if i - j in ldic:
                    ldic[i - j].append((i, j))
                else:
                    ldic[i - j] = [(i, j)]

                if j + i - self.height in rdic:
                    rdic[j + i - self.height].append((i, j))
                else:
                    rdic[j + i - self.height] = [(i, j)]

        result = hdic.values()
        result.extend(vdic.values())
        result.extend(ldic.values())
        result.extend(rdic.values())
        self.ox_list = result

    def count(self, state, ox_list):
        """
        Count the 'ox' in a row
        Return a dict contain all the numbers of x in a row and o's.
        """
        result = {'x': [], 'o': []}
        for ox in result.keys():
            c = 0
            head_available = False
            for i in ox_list:
                if state.board[i] == ox:
                    c += 1
                elif state.board[i] is None:
                    result[ox].append(c)
                    head_available = True
                    c = 0
                else:
                    if head_available or c >= 4:
                        result[ox].append(c)
                    head_available = False
                    c = 0
                if head_available or c >= 4:
                    result[ox].append(c)
            result[ox].append(c)
        return result

    def eval(self, state):
        """
        When there are 4 x in a row, return inf
        If there are 4 o in a row, return -inf
        Else return 3 * C3(x) + 1 * C2(x) -  3 * C3(o) + 1 * C2(o)
        """
        result = {'x': [], 'o': []}
        for ox_list in self.ox_list:
            counts = self.count(state, ox_list)
            if counts['x'] and max(counts['x']) >= 4:
                return float('inf')
            elif counts['o'] and max(counts['o']) >= 4:
                return -float('inf')
            else:
                for ox in result.keys():
                    result[ox].extend(counts[ox])
        points = {3: 3, 2: 1, 1: 0, 0: 0}
        eval_score = {'x': 0, 'o': 0}
        for ox, counts in result.items():
            for c in counts:
                eval_score[ox] += points[c]
        return eval_score['x'] - eval_score['o']

    def win(self, state, ox=None):
        """
        When there 4 x or 4 o in a row, return True
        Otherwise return False
        """
        for ox_list in self.ox_list:
            counts = self.count(state, ox_list)
            if counts['x'] and max(counts['x']) >= 4:
                if not ox:
                    return True
                elif ox == 'x':
                    return True
            elif counts['o'] and max(counts['o']) >= 4:
                if not ox:
                    return True
                elif ox == 'o':
                    return True
        return False
