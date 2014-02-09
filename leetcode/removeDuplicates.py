class Solution:
    # @param a list of integers
    # @return an integer

    def removeDuplicates(self, A):
        length = len(A)
        i = 0
        duplicated = 0
        last = None
        while i < length:
            if A[i] == last:
                duplicated += 1
            else:
                # remove
                if duplicated:
                    A[i - duplicated:] = A[i:]
                    i -= duplicated
                    length -= duplicated
                duplicated = 0
            last = A[i]
            i += 1
        if duplicated:
            A[i - duplicated:] = A[i:]
            length -= duplicated
        return length


if __name__ == '__main__':
    s = Solution()
    a = [1, 1, 2, 3, 4, 4]
    print s.removeDuplicates(a)
    print a
    # print a
