class Solution:
    # @param n, an integer
    # @return an integer
    dic = {1: 1, 2: 2}

    def climbStairs(self, n):
        if n in self.dic:
            return self.dic[n]
        tmp = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.dic[n] = tmp
        return tmp
