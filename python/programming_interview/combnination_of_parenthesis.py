def parenthesis(n):
    stack = []
    stack.append(('(', 1, 0, '('))
    while stack:
        p = stack.pop()
        if p[1] < n:
            stack.append(('(', p[1] + 1, p[2], p[3] + '('))
        if p[1] > p[2] and p[2] < n:
            stack.append((')', p[1], p[2] + 1, p[3] + ')'))
        if p[1] == n and p[2] == n:
            # leaf return path
            yield p[3]


def recursive_p(n):
    path = []
    left = 0
    right = 0

    def helper(path, left, right):
        if left < n:
            path.append('(')
            left += 1
            for i in helper(path, left, right):
                yield i
            path.pop()
            left -= 1
        if right < n and left > right:
            path.append(')')
            right += 1
            for i in helper(path, left, right):
                yield i
            path.pop()
            right -= 1
        if left == n and right == n:
            yield ''.join(path)

    return helper(path, left, right)


def main():
    for i in parenthesis(3):
        print i
    print ''
    for i in recursive_p(3):
        print i

if __name__ == '__main__':
    main()
