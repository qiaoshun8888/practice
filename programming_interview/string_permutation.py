"""
print permutation
"""
import sys


def p1(s):
    """
    dfs with stack
    """
    stack = []
    visited = []
    stack.append("")
    while stack:
        node = stack.pop()
        permutation = ''.join([s[int(i)] for i in node])
        if permutation not in visited:
            if len(node) == len(s):
                pass
                # print permutation
            for i in range(len(s)):
                if str(i) not in node:
                    stack.append(node + str(i))
            visited.append(permutation)
    # print sys.getsizeof(visited)


def p2(s, visited=[]):
    '''recursive'''
    def helper(res):
        permutation = ''.join([s[i] for i in res])
        if permutation not in visited:
            if len(permutation) == len(s):
                print permutation
            else:
                for i in range(len(s)):
                    if i not in res:
                        res.append(i)
                        helper(res)
                        res.pop()
                visited.append(permutation)
    helper([])


def p3(s):
    def helper(s, index):
        current = index
        if current == len(s) - 1:
            print ''.join(s)
            return

        helper(s, current + 1)

        for i in range(current + 1, len(s)):
            s[current], s[i] = s[i], s[current]
            helper(s, current + 1)
    helper(list(s), 0)


def main():
    p3("test")

if __name__ == '__main__':
    main()
