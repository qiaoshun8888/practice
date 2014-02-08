class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def get_col(self, col):
        if col > self.width - 1:
            return []

        res = []
        for i in range(self.height):
            res.append(self.matrix[i][col])
        return res

    def rotate(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        result = []
        for i in range(self.width):
            result.append(self.get_col(i)[::-1])
        return result
