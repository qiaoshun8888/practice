
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import copy
from structs import binary_tree


def maximum_path_sum(t):

    if not t:
        t = [[3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3]]
    if t:
        t = t.split('\n')
        for k, v in enumerate(t):
            t[k] = [int(i) for i in v.strip().split(' ')]

    for i, r in enumerate(t[::-1]):
        for k, v in enumerate(r):
            r[k] = binary_tree.Node(v)
            if i > 0:
                r[k].left = t[-i][k]
                r[k].right = t[-i][k + 1]

    def path_sums():
        root = t[0][0]
        stack = []
        stack.append((root, 0, []))
        while stack:
            e, res, path = stack.pop()
            tmppath = copy.copy(path)
            tmppath.append(e.data)
            if e.left:
                stack.append((e.left, res + e.data, tmppath))
            if e.right:
                stack.append((e.right, res + e.data, tmppath))
            if not e.left and not e.right:
                # leaf
                yield res + e.data, tmppath

    best = 0
    best_path = []
    for i, j in path_sums():
        if i > best:
            best = i
            best_path = j
    return best, best_path


if __name__ == '__main__':
    print maximum_path_sum("""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""")
