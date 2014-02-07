class Solution:
    # @return an integer
    dic = {0: 1, 1: 1, 2: 2}

    def numTrees(self, n):
        if n in self.dic:
            return self.dic[n]

        res = 0
        for i in range(n):
            l = self.numTrees(i)
            r = self.numTrees(n - i- 1)
            res += l * r
        self.dic[n] = res
        return res


if __name__ == '__main__':
    s = Solution()
    print s.numTrees(14)
