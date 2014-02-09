class Solution:
    # @return a boolean

    def isValid(self, s):
        stack = [s[0]]
        for i in s[1:]:
            if i in ')]}':
                if not stack:
                    return False
                if i == ')' and not stack[-1] == '(':
                    return False
                if i == ']' and not stack[-1] == '[':
                    return False
                if i == '}' and not stack[-1] == '{':
                    return False
                stack.pop()
            if i in '([{':
                stack.append(i)
        if not stack:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print s.isValid('[])')
