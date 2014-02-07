class Solution:
    # @param a list of integers
    # @return an integer

    def removeDuplicates(self, A):
        dup_len = 0
        k = 0
        tmp = None
        a_len = len(A)
        while k < a_len:
            if A[k] == tmp:
                dup_len += 1
            else:
                A[k - dup_len:] = A[k:]
                k -= dup_len
                tmp = A[k]
                a_len -= dup_len
                dup_len = 0

            k += 1
        return a_len

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates(range(-999, 999))
