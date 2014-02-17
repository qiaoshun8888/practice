
class Solution:
    # @param s, a string
    # @return an integer

    def lengthOfLastWord(self, s):
        return len(s.strip().split(' ')[-1])


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLastWord('Hello World')
