class Solution:
    # @return a string
    dic = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }

    def intToRoman(self, num):
        keys = sorted(self.dic.keys())

        def helper(num, keys, res):
            if num > 0:
                m = keys.pop()
                # print m
                d = num / m
                res += "".join([self.dic[m]] * d)
                res = helper(num % m, keys, res)
            return res

        s = helper(num, keys, "")
        s = s.replace('DCCCC', 'CM')
        s = s.replace('CCCC', 'CD')
        s = s.replace('LXXXX', 'XC')
        s = s.replace('XXXX', 'XL')
        s = s.replace('VIIII', 'IX')
        s = s.replace('IIII', 'IV')
        return s


if __name__ == '__main__':
    s = Solution()
    print s.intToRoman(9)
