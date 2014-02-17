class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer

    def subsets(self, S):
        S.sort()
        size = len(S)
        subsets = []
        for i in range(1 << size):
            # print i, bin(i)[2:]
            subset = []
            for k, v in enumerate(bin(i)[2::][::-1]):
                if v == '1':
                    subset.append(S[k])
            subsets.append(subset)
        return subsets

if __name__ == '__main__':
    s = Solution()
    print s.subsets([1, 2])
