class Solution:

    def get_col(self, col):
        res = []
        for i in range(len(self.matrix)):
            res.append(self.matrix[i][col])
        return res

    def print_spiral(self, matrix):
        self.matrix = matrix
        # line
        left = 0
        top = 0
        right = len(self.matrix[0]) - 1
        bottom = len(self.matrix) - 1

        while left <= right or top <= bottom:
            # print left, right, top, bottom
            if top <= bottom:
                for i in self.matrix[top][left:right + 1]:
                    print i,
                top += 1
            if left <= right:
                for i in self.get_col(right)[top:bottom + 1]:
                    print i,
                right -= 1
            if top <= bottom:
                for i in self.matrix[bottom][left:right + 1][::-1]:
                    print i,
                bottom -= 1
            if left <= right:
                for i in self.get_col(left)[top:bottom + 1][::-1]:
                    print i,
                left += 1

if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    s.print_spiral(matrix)
