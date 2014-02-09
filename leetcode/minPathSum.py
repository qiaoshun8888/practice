class Solution:
    # @param grid, a list of lists of integers
    # @return an integer

    def minPathSum(self, grid):
        if not grid:
            return 0
        minimum = float('inf')
        m = len(grid) - 1
        n = len(grid[0]) - 1
        if m == 0 and n == 0:
            return grid[0][0]
        d = [[None] * (n + 1) for i in range(m + 1)]
        d[0][0] = grid[0][0]
        for i in range(1, n + 1):
            d[0][i] = d[0][i - 1] + grid[0][i]
        for i in range(1, m + 1):
            d[i][0] = d[i - 1][0] + grid[i][0]

        if m == 0:
            return d[0][-1]
        if n == 0:
            return d[-1][0]

        stack = [(1, 1)]
        visited = set()
        while stack:
            node = stack.pop(0)
            if node[0] < m:
                p = (node[0] + 1, node[1])
                if p not in visited:
                    stack.append(p)
                    visited.add(p)
            if node[1] < n:
                p = (node[0], node[1] + 1)
                if p not in visited:
                    stack.append(p)
                    visited.add(p)
            d[node[0]][node[1]] = min(d[node[0] - 1][node[1]], d[
                                      node[0]][node[1] - 1]) + grid[node[0]][node[1]]
        for i in d:
            print i
        return d[m][n]

        # print d[1][0]
        # print grid[1][0]

        # stack = [((0, 0), grid[0][0])]
        # visited = set()
        # while stack:
        #     node, s = stack.pop()
        # print n\\ode, s
        #     if node[0] == m and node[1] == n:
        #         if s < minimum:
        #             minimum = s
        #     else:
        #         if node[0] < m:
        #             p = (node[0] + 1, node[1])
        # if p not in visited:
        #             stack.append((p, s + grid[p[0]][p[1]]))
        #         if node[1] < n:
        #             p = (node[0], node[1] + 1)
        # if p not in visited:
        #             stack.append((p, s + grid[p[0]][p[1]]))
        # visited.add(node)
        # return minimum


def main():
    # grid = [[1]]
    # grid = [
    #     [7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
    #     [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
    #     [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
    #     [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
    #     [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
    #     [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
    #     [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
    #     [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
    #     [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
    #     [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
    #     [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
    #     [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9]
    # ]
    # grid = [[1, 2], [1, 1]]
    grid = [[9, 1, 4, 8]]
    s = Solution()
    print s.minPathSum(grid)


if __name__ == '__main__':
    main()
