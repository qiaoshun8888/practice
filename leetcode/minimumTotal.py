class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution1:
    # @param triangle, a list of lists of integers
    # @return an integer

    def buildTree(self, triangle):

        triangle[0][0] = Node(triangle[0][0])
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] = Node(triangle[i][j])
                if j < len(triangle[i]) - 1:
                    triangle[i - 1][j].left = triangle[i][j]
                if j >= 1:
                    triangle[i - 1][j - 1].right = triangle[i][j]

    def minimumTotal(self, triangle):
        if not triangle:
            return None
        self.buildTree(triangle)
        # DFS won't work
        minimum = float('+inf')

        stack = [(triangle[0][0], triangle[0][0].val)]
        while stack:
            node, sum = stack.pop()
            if not node.left and not node.right:
                minimum = min(sum, minimum)
            else:
                if node.left:
                    stack.append((node.left, sum + node.left.val))
                if node.right:
                    stack.append((node.right, sum + node.right.val))
        return minimum


class Solution:

    def minimumTotal(self, triangle):
        if not triangle:
            return None
        # self.buildTree(triangle)

        d = list(triangle)

        for i in range(1, len(d)):
            for j in range(len(d[i])):
                lp = float('inf')
                rp = float('inf')
                if j < len(d[i]) - 1:
                    rp = d[i - 1][j]
                if j >= 1:
                    lp = d[i - 1][j - 1]
                d[i][j] += min(lp, rp)
        return min(d[len(d) - 1])


if __name__ == '__main__':
    s = Solution()
    triangle = [
        [-7],
        [-2, 1],
        [-5, -5, 9],
        [-4, -5, 4, 4],
        [-6, -6, 2, -1, -5],
        [3, 7, 8, -3, 7, -9],
        [-9, -1, -9, 6, 9, 0, 7],
        [-7, 0, -6, -8, 7, 1, -4, 9],
        [-3, 2, -6, -9, -7, -6, -9, 4, 0],
        [-8, -6, -3, -9, -2, -6, 7, -5, 0, 7],
        [-9, -1, -2, 4, -2, 4, 4, -1, 2, -5, 5],
        [1, 1, -6, 1, -2, -4, 4, -2, 6, -6, 0, 6],
        [-3, -3, -6, -2, -6, -2, 7, -9, -5, -7, -5, 5, 1]]
    print s.minimumTotal(triangle)
