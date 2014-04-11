class Solution:
    # @param a list of integers
    # @return an integer

    def removeDuplicates(self, A):
        if not A:
            return 0
        tmp, removed = A[0],  0
        for k, v in enumerate(A[1:]):
            if tmp == v:
                removed += 1
            else:
                A[k - removed + 1] = A[k + 1]
            tmp = v
        return len(A) - removed


if __name__ == '__main__':
    s = Solution()
    a = []
    print s.removeDuplicates(a), a
    a = [1, 1, 2]
    print s.removeDuplicates(a), a
    a = [1, 1, 2, 3, 4, 4]
    print s.removeDuplicates(a), a
    a = [1, 1, 1, 1, 1, 1, 1, 1]
    print s.removeDuplicates(a), a
