class Solution:
    # @return a list of integers
    dic = {1: [0, 1]}

    def grayCode(self, n):
        if n < 1:
            return [0]
        for i in range(2, n + 1):
            ext = []
            for j in self.dic[i - 1][::-1]:
                ext.append(j + (1 << (i - 1)))
            self.dic[i] = self.dic[i - 1] + ext
        return self.dic[n]


if __name__ == '__main__':
    s = Solution()
    print s.grayCode(0)
