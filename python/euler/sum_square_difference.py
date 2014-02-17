
def sum_square_difference(n):
    s1 = 0
    s2 = 0
    for i in range(n + 1):
        s1 += i ** 2
        s2 += i
    s2 = s2 ** 2
    return s2 - s1

if __name__ == '__main__':
    print sum_square_difference(100)
