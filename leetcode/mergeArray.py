class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing

    def merge(self, A, m, B, n):
        i, j = 0, 0
        while i < m and j < n:
            if A[i] > B[j]:
                A[i + 1:] = A[i:]
                A[i] = B[j]
                j += 1
                m += 1
            i += 1

        if j < n:
            A[m:] = B[j:]
