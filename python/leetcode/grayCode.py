class Solution:
    # @return a list of integers

    def grayCode(self, n):
        dic = {0: [0], 1: [0, 1]}
        for i in range(2, n + 1):
            dic[i] = dic[i - 1] + [j + (1 << (i - 1)) for j in dic[i - 1][::-1]]
        return dic[n]


if __name__ == '__main__':
    s = Solution()
    print s.grayCode(0)
