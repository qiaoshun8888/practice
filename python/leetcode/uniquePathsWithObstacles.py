class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer

    def uniquePathsWithObstacles(self, obstacleGrid):

        def helper(x, y, dic):
            if obstacleGrid[x][y]:
                return 0
            if x <= 0 and y <= 0:
                return 1
            if (x, y) in dic:
                return dic[(x, y)]

            res = 0
            if x > 0 and obstacleGrid[x - 1][y] == 0:
                res += helper(x - 1, y, dic)
            if y > 0 and obstacleGrid[x][y - 1] == 0:
                res += helper(x, y - 1, dic)
            dic[(x, y)] = res
            return res
        return helper(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1, {})

if __name__ == '__main__':
    s = Solution()
    grid = [
        [0, 0, 1],
    ]
    print s.uniquePathsWithObstacles(grid)
