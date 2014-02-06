def dfs_with_stack(n):
    stack = []
    stack.append({'res': '(', 'left': 1, 'right': 0})
    while stack:
        node = stack.pop()
        if node['left'] < n:
            stack.append({'res': node['res'] + '(',
                          'left': node['left'] + 1,
                          'right': node['right']})
        if node['right'] < n and node['left'] > node['right']:
            stack.append({'res': node['res'] + ')',
                          'left': node['left'],
                          'right': node['right'] + 1})
        if node['left'] == node['right'] == n:
            yield node['res']


def dfs_recursive(n):
    def dfs_helper(res, left, right):
        if left < n:
            res += '('
            left += 1
            for i in dfs_helper(res, left, right):
                yield i
            res = res[:-1]
            left -= 1
        if right < n and left > right:
            res += ')'
            right += 1
            for i in dfs_helper(res, left, right):
                yield i
            res = res[:-1]
            right -= 1
        if left == n and right == n:
            yield res
    return dfs_helper('', 0, 0)


def parentheses(n):
    '''
    This is wrong, a little bit right :(
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
    # print parentheses(3)
    for i in dfs_with_stack(3):
        print i
    print ''
    for i in dfs_recursive(3):
        print i
