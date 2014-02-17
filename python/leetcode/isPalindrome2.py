class Solution:
    # @param s, a string
    # @return a boolean

    def isPalindrome(self, s):
        def is_word(i):
            if ord(i.lower()) in range(48, 58):
                return True
            elif ord(i.lower()) in range(97, 123):
                return True
            return False

        i = 0
        j = len(s) - 1
        while i < j:
            while not is_word(s[i]) and i < j:
                i += 1
            while not is_word(s[j]) and i < j:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome('A man, a plan, a canal: Panama')
    print s.isPalindrome('race a car')
    print s.isPalindrome('.,')
    print s.isPalindrome('1a2')
