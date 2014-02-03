"""
Jigsaw puzzle
"""
import random


class Piece():

    """
    user cannot access to _id
    """

    def __init__(self, _id, puzzle):
        self._id = _id
        self.puzzle = puzzle

    def _set_relations(self):
        if self._id - self.puzzle.m in range(self.puzzle.m * self.puzzle.n):
            self.top = self.puzzle.pieces[self._id - self.puzzle.m]
        if self._id + self.puzzle.m in range(self.puzzle.m * self.puzzle.n):
            self.bottom = self.puzzle.pieces[self._id + self.puzzle.m]
        if self._id - 1 in range(self.puzzle.m * self.puzzle.n):
            self.left = self.puzzle.pieces[self._id - 1]
        if self._id + 1 in range(self.puzzle.m * self.puzzle.n):
            self.right = self.puzzle.pieces[self._id + 1]


class Puzzle():

    def __init__(self, m, n):
        self.pieces = []
        self.m = m
        self.n = n

        for i in range(m * n):
            # print i
            p = Piece(i, self)
            self.pieces.append(p)

        for i in self.pieces:
            i._set_relations()

    def draw(self):
        if self.pieces:
            yield self.pieces[random.randrange(len(self.pieces))]

    def fitwith(self, p1, p2):
        if hasattr(p1, 'left') and p1.left == p2:
            p1.get_left = p2
            return True
        elif hasattr(p1, 'right') and p1.right == p2:
            p1.get_right = p2
            return True
        elif hasattr(p1, 'top')and p1.top == p2:
            p1.get_top = p2
            return True
        elif hasattr(p1, 'bottom')and p1.bottom == p2:
            p1.get_bottom = p2
            return True
        return False


if __name__ == '__main__':
    p = Puzzle(8, 8)
    head = None
    for i in p.pieces:
        for j in p.pieces:
            if i == j:
                continue
            else:
                p.fitwith(i, j)
                # for n in ['get_left', 'get_right', 'get_top', 'get_bottom']:
                #     if not hasattr(i, n):
                #         continue
                # p.pieces.remove(i)
        # print i._id
        # print i.get_right

    head = p.pieces[0]
    while head:
        print head._id
        if not hasattr(head, 'get_right'):
            break
        head = head.get_right
