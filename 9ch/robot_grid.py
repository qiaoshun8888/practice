"""
Imagine a robot sitting on the upper left corner of an X by Y grid
The robot can only move in two directions: right and down
How many possible paths are there
From 0, 0 to X, Y
"""


def ways(x, y, blocked=[]):
    dic = {}

    def ways_from(a, b):
        if a == x and b == y:
            return 1
        if "%d:%d" % (a, b) in dic:
            return dic["%d:%d" % (a, b)]

        r = 0
        if a + 1 <= x and (a + 1, b) not in blocked:
            r += ways_from(a + 1, b)
        if b + 1 <= y and (a, b + 1) not in blocked:
            r += ways_from(a, b + 1)
        dic["%d:%d" % (a, b)] = r
        return r
    return ways_from(0, 0)


def main():
    print ways(5, 5, [(1, 1), (2, 2), (3, 3)])

if __name__ == '__main__':
    main()
