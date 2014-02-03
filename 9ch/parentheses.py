def parentheses(n):
    '''
    This is wrong, a little bit :(
    '''
    if n == 1:
        return ['()']
    res = set()
    s = parentheses(n - 1)
    # s = ['()()', '(())']
    for i in range(len(s)):
        for j in range(2 * (n - 1) - 1):
            for k in range(j, 2 * (n - 1)):
                # print j, k
                # print j, k, s[i], s[i][:j], s[i][j:k], s[i][k:]
                res.add(s[i][:j] + '(' + s[i][j:k] + ')' + s[i][k:])
    return list(res)

if __name__ == '__main__':
    print parentheses(3)
