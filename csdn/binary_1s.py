'''
28

how many 1 in binary format
'''


def c(n):
    c = 0
    for i in bin(n)[2:]:
        if i == '1':
            c += 1
    return c


def c1(n):
    c = 0
    while n > 1:
        if n % 2:
            c += 1
        n /= 2
    return c + 1


def c2(n):
    c = 0
    while n > 1:
        if n & 1:
            c += 1
        n = n >> 1
    return c + 1


if __name__ == '__main__':
    print c2(10)
