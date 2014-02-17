class Solution:
    # @return an integer

    def uniquePaths(self, m, n):
        def f(a, b=0):
            r = 1
            for i in range(b + 1, a + 1):
                r *= i
            return r

        def c(a, b):
            return f(a, a - b) / f(b)

        total = m - 1 + n - 1
        return c(total, m - 1)
