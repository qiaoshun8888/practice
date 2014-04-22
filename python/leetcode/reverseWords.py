class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # strip for ' '
        tmp = []
        for i in s.split(' ')[::-1]:
            i = i.strip()
            if i:
                tmp.append(i)
        return ' '.join(tmp)

if __name__ == '__main__':
    s = Solution()
    print s.reverseWords('the sky is blue');
