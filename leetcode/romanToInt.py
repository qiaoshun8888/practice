class Solution:
    # @return an integer
    dic = {
        'I':   1,
        'V':   5,
        'X':   10,
        'L':   50,
        'C':   100,
        'D':   500,
        'M':   1000,
    }

    def romanToInt(self, s):
        s = s.replace('IV', 'IIII')
        s = s.replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX')
        s = s.replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC')
        s = s.replace('CM', 'DCCCC')
        # print s
        r = 0
        for i in s:
            r += self.dic[i]
        return r

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt('MCMXCVI')
