class Solution:
    # @param A, a list of integer
    # @return an integer

    def singleNumber(self, A):
        r = 0
        for i in A:
            r ^= i
        return r


if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([2, 2, 3, 1, 3])
