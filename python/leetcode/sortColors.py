class Solution:
    # @param A a list of integers
    # @return nothing, sort in place

    def sortColors(self, A):
        dic = {0: 0, 1: 0, 2: 0}
        for i in A:
            dic[i] += 1

        p = 0
        for i in range(3):
            print p, p + dic[i], i
            A[p: p + dic[i]] = [i] * dic[i]
            p = p + dic[i]
        return A


if __name__ == '__main__':
    s = Solution()
    print s.sortColors([1, 0, 2, 2, 1, 1, 1, 1, 0, 0])
