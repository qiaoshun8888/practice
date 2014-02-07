class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        current = 0
        best = 0
        for i in A:
            current += i
            if current < 0:
                current = 0
            if current > best:
                best = current
        return best
