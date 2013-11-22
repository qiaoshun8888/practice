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
        if self.win('x', state) or self.win('o', state):
            return True
        return False

    def terminal_result(self, state):
        """
        Given state, return the terminal state description
        Should only be called when terminal_test is True
        """
        if self.win('x', state) and not self.win('o', state):
            return 'X!'
        elif not self.win('x', state) and self.win('o', state):
            return 'O!'
        elif not self.actions(state):
            return 'Draw!'
        else:
            return 'Not over'

    def subcon(self, ox, block, direction, state):
        '''
        Given player symbol, position, direction, state
        Return how many
        '''
        c = 1
        breaks = 0
        for d in direction:
            (tmp_i, tmp_j) = block
            tmp_i += d[0]
            tmp_j += d[1]
            while True:
                if tmp_i > self.height - 1 or tmp_j > self.width - 1 or tmp_i < 0 or tmp_j < 0:
                    breaks += 1
                    break
                if not state.board[(tmp_i, tmp_j)] == ox:
                    if state.board[(tmp_i, tmp_j)]:
                        breaks += 1
                    break
                else:
                    c += 1
                    tmp_i += d[0]
                    tmp_j += d[1]
        if breaks == 2 and c < 4:  # and c >= 2:
            c = 1
        return c

    directions = (((0, 1), (0, -1)),
                 ((1, 1), (-1, -1)),
                 ((1, 0), (-1, 0)),
                 ((1, -1), (-1, 1)))

    def win(self, ox, state):
        for k, v in state.board.items():
            if v == ox:
                for direction in self.directions:
                    subcon = self.subcon(ox, k, direction, state)
                    if subcon >= 4:
                        return True
        return False

    # def count(self, state, ox_list):
    #     result = {'x': [], 'o': []}
    #     for ox in result.keys():
    #         c = 0
    #         for i in ox_list:
    #             if state.board[i] == ox:
    #                 c += 1
    #             elif not state.board[i]:
    #                 if c > 0:
    #                     result[ox].append(c)
    #                 head_cut = False
    #                 c = 0
    #             else:
    #                 if not head_cut or c >= 4:
    #                     result[ox].append(c)
    #                 c = 0

    #         if (c > 0 and not head_cut) or c >= 4:
    #             result[ox].append(c)
    #     # print result
    #     return result

    # def get_ox_list(self):
    #     hdic = {}
    #     vdic = {}
    #     ldic = {}
    #     rdic = {}
    #     for i in range(self.height):
    #         for j in range(self.width):
    #             if i in hdic:
    #                 hdic[i].append((i, j))
    #             else:
    #                 hdic[i] = [(i, j)]

    #             if j in vdic:
    #                 vdic[j].append((i, j))
    #             else:
    #                 vdic[j] = [(i, j)]

    #             if i - j in ldic:
    #                 ldic[i - j].append((i, j))
    #             else:
    #                 ldic[i - j] = [(i, j)]

    #             if j + i - self.height in rdic:
    #                 rdic[j + i - self.height].append((i, j))
    #             else:
    #                 rdic[j + i - self.height] = [(i, j)]

    #     result = hdic.values()
    #     result.extend(vdic.values())
    #     result.extend(ldic.values())
    #     result.extend(rdic.values())
    #     return result

    def eval(self, state):
        '''
        count
        '''
        # result = {'x': [], 'o': []}
        # for ox_list in self.get_ox_list():
        #     counts = self.count(state, ox_list)
        #     if counts['x'] and max(counts['x']) >= 4:
        #         return 1
        #     elif counts['o'] and max(counts['o']) >= 4:
        #         return -1
        #     else:
        #         for ox in result.keys():
        #             result[ox].extend(counts[ox])
        # # print result
        # #
        # points = {3: 3, 2: 1, 1: 0}
        # eval_score = {'x': 0, 'o': 0}
        # for ox, counts in result.items():
        #     for c in counts:
        #         eval_score[ox] += points[c]

        # print '================================'
        # print eval_score['x'] - eval_score['o']
        # state.display()
        # print '================================'
        # return eval_score['x'] - eval_score['o']
        result = {'x': 0, 'o': 0}
        # points = {3: 3, 2: 1, 1: 0}
        for ox in result.keys():
            for k, v in state.board.items():
                if v == ox:
                    for direction in self.directions:
                        subcon = self.subcon(ox, k, direction, state)
                        if subcon > result[ox]:
                            result[ox] = subcon
                        # if subcon >= 4:
                        #     return 1 if ox == 'x' else -1
                        # result[ox] += points[subcon]
        return result['x'] - result['o']
