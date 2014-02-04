"""
too slow
come on
improve it!
"""
import math


def digit_factorials(dn):
    d = {}

    def digits(n, d):
        f = 0
        for i in str(n):
            f += math.factorial(int(i))
        return f

    for i in range(3, 10 ** dn):
        f = digits(i, d)
        if f == i:
            yield i

    for i in range(10 ** 6, 2540160):
        f = digits(i, d)
        if f == i:
            yield i

if __name__ == '__main__':
    n = 0
    for i in digit_factorials(5):
        n += i
    print n
