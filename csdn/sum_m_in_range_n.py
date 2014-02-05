'''
# 21
'''


def find(n, m):
    if m < 2 or m > 2 * n:
        raise ValueError
    for i in range(1, min(n + 1, m)):
        yield i, m - i


def main():
    for i in find(8, 4):
        print i

if __name__ == '__main__':
    main()
