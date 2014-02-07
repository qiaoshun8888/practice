class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer

    def searchInsert(self, A, target):
        def helper(A, start, end, target):
            if end < start:
                raise ValueError
            if end == start:
                if A[start] >= target:
                    return start
                else:
                    return start + 1
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                return helper(A, start, max(start, mid - 1), target)
            else:
                return helper(A, min(mid + 1, end), end, target)
        return helper(A, 0, len(A) - 1, target)


if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1, 3, 5, 6], 5)
    print s.searchInsert([1, 3, 5, 6], 2)
    print s.searchInsert([1, 3, 5, 6], 7)
    print s.searchInsert([1, 3, 5, 6], 0)
    print s.searchInsert([1, 3], 0)
