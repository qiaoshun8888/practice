import math


def factorial_digit_sum(n):
    f = math.factorial(n)

    s = 0
    for i in str(f):
        s += int(i)
    return s


if __name__ == '__main__':
    print factorial_digit_sum(100)
