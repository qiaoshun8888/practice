'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''


class Solution:
    # @return a list of lists of integer

    def generateMatrix(self, n):
        # 1,1 -> 1,n
        # 2,n -> n,n
        # n,n-1 -> n,1
        # n-1,1 -> 2,1
        matrix = [[0] * n for i in range(n)]
        val = 1
        top = 0
        left = 0
        bottom = n - 1
        right = n - 1
        while val <= n ** 2:
            if top <= bottom:
                # top
                for i in range(left, right + 1):
                    matrix[top][i] = val
                    val += 1
                top += 1
            if left <= right:
                # right
                for i in range(top, bottom + 1):
                    matrix[i][right] = val
                    val += 1
                right -= 1
            if top <= bottom:
                # bottom
                for i in range(left, right + 1)[::-1]:
                    matrix[bottom][i] = val
                    val += 1
                bottom -= 1
            if left <= right:
                # left
                for i in range(top, bottom + 1)[::-1]:
                    matrix[i][left] = val
                    val += 1
                left += 1

        return matrix

if __name__ == '__main__':
    s = Solution()
    for i in s.generateMatrix(4):
        print i
