class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float

    def pow(self, x, n):
        if n < 0:
            return 1 / self.pow(x, -n)
        elif n == 0 or x == 1:
            return 1
        elif n == 1:
            return x
        else:
            if x == -1 and n % 2 == 1:
                return -1
            if  x == -1 and n % 2 == 0:
                return 1
            t = self.pow(x, n / 2)
            if n % 2:
                return x * t * t
            else:
                return t * t

if __name__ == '__main__':
    s = Solution()
    print s.pow(0.00001, 2147483647)

