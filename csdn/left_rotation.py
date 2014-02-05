'''
# 28
string left rotation

maybe some tricky in c ++??? don't know yet
'''


def py_lr(s, n):
    return s[n:] + s[:n]


def main():
    print py_lr('abcdef', 2)


if __name__ == '__main__':
    main()
