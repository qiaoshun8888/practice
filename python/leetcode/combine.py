class Solution:
    # @return a list of lists of integers

    def combine(self, n, k):
        if k > n:
            raise ValueError
        if k == n:
            return [range(1, n + 1)]

        def helper(pool, k, subset):
            if k == 0:
                yield subset
            else:
                pool = list(pool)
                while pool:
                    subset.append(pool.pop(0))
                    for i in helper(pool, k - 1, subset):
                        yield i
                    subset.pop()
        result = []
        for i in helper(range(1, n + 1), k, []):
            result.append(list(i))
        return result

if __name__ == '__main__':
    s = Solution()
    print s.combine(3, 2)
