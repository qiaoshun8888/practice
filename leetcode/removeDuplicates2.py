class Solution:
    # @param A a list of integers
    # @return an integer

    def removeDuplicates(self, A):
        last = None
        length = len(A)
        i = 0
        duplicate = 0
        while i < length:
            if A[i] == last:
                duplicate += 1
            else:
                if duplicate >= 2:
                    # remove dumplicate - 1
                    A[i - duplicate + 1:] = A[i:]
                    i -= duplicate - 1
                    length -= duplicate - 1
                duplicate = 0
            last = A[i]
            i += 1
        if duplicate >= 2:
            A[i - duplicate + 1:] = A[i:]
            length -= duplicate - 1
        return length

s = Solution()
a = [1, 1, 1]
print s.removeDuplicates(a)
print a
