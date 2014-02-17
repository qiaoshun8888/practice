class Solution:
    # @return a list of strings, [s1, s2]

    def letterCombinations(self, digits):
        if not digits:
            return ['']
        d2l = {
            2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
            6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        res = []
        i = digits[0]
        rest = digits[1:]
        rest_combine = self.letterCombinations(rest)
        for c in rest_combine:
            for l in d2l[int(i)]:
                res.append(l + c)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.letterCombinations('345')
