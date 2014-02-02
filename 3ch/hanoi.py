"""
tower of hanoi
"""


class Hanoi:
    stacks = {1: [], 2: [], 3: []}

    def __init__(self, n):
        self.stacks[1] = range(1, n + 1)[::-1]

    def get_other_tower(self, f, to):
        for i in range(1, 4):
            if i not in [f, to]:
                return i
        print 'Error'
        return -1

    def move(self, n=None, f=1, to=3):
        if not n:
            n = len(self.stacks[f])
        if n > 1:
            theother = self.get_other_tower(f, to)
            if self.stacks[f]:
                self.move(n - 1, f, theother)
                for v in self.stacks.values():
                    print v,
                print ""

            self.stacks[to].append(self.stacks[f].pop())
            for v in self.stacks.values():
                print v,
            print ""

            if self.stacks[theother]:
                self.move(n - 1, theother, to)
                for v in self.stacks.values():
                    print v,
                print ""

        else:
            self.stacks[to].append(self.stacks[f].pop())

h = Hanoi(10)
h.move()
