class Solution:
    # @return a boolean

    def getlength(self, x):
        k = 1
        while 10 ** k <= x:
            k += 1
        return k

    def getdigit(self, x, d):
        return (x % (10 ** (d + 1))) / (10 ** d)

    def isPalindrome(self, x):
        if x < 0:
            return False

        length = self.getlength(x)
        if length == 1:
            return True

        for i in range(length / 2):
            if not self.getdigit(x, i) == self.getdigit(x, length - i - 1):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(10)
