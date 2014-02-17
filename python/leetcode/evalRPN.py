class Solution:
    # @param tokens, a list of string
    # @return an integer

    def add(self, n1, n2):
        return n1 + n2

    def minus(self, n1, n2):
        return n1 - n2

    def multiple(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        return n1 / n2

    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                if i == '+':
                    ti = 'add'
                elif i == '-':
                    ti = 'minus'
                elif i == '*':
                    ti = 'multiple'
                elif i == '/':
                    ti = 'divide'
                n2 = stack.pop()
                n1 = stack.pop()
                res = getattr(self, ti)(n1, n2)
                stack.append(res)
                print n1, i, n2, '=', res
        if stack:
            return stack.pop()
        else:
            raise ValueError

if __name__ == '__main__':
    s = Solution()
    print s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
