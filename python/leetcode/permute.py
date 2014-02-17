class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers

    def permute(self, num):
        def helper(num, res):
            for i in num:
                if i not in res:
                    res.append(i)
                    for i in helper(num, res):
                        yield i
                    res.pop()

            if len(res) == len(num):
                yield res

        permutes = []
        for i in helper(num, []):
            r = []
            for j in i:
                r.append(j)
            permutes.append(r)

        return permutes


def helper(num, res):
    for i in num:
        if i not in res:
            res.append(i)
            for i in helper(num, res):
                yield i
            res.pop()

    if len(res) == len(num):
        yield res

if __name__ == '__main__':
    s = Solution()

    for i in s.permute([1, 2, 3]):
        print i
