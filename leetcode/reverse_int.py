class Solution:
    # @return an integer

    def reverse(self, x):
        neg = False
        if x < 0:
            neg = True
            x = -x
        r = int(str(x)[::-1])
        return r if not neg else -r


if __name__ == '__main__':
    s = Solution()
    print s.reverse(123)
