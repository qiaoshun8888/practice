class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer

    def removeElement(self, A, elem):
        length = len(A)
        k = 0
        while k < length:
            if A[k] == elem:
                A.pop(k)
                length -= 1
            else:
                k += 1

        return length


if __name__ == '__main__':
    s = Solution()
    print s.removeElement([1, 2, 3, 4, 5], 3)
