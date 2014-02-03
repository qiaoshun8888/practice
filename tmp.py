import math


def fib(n):
    f = {}
    for i in range(n + 1)[1:]:
        if i <= 2:
            f[i] = 1
        else:
            f[i] = f[i - 1] + f[i - 2]
    return f[n]



d = {}


# def coin_sums(n):
#     choices = [1, 2, 5, 10, 20, 50, 100, 200]
#     r = 0
#     if n == 1:
#         return 1
#     if n in choices:
#         r = 1

#     ed = []
#     for i in choices:
#         if i < n:
#             r += coin_sums(n - i) / 2
#     return r

def self_powers(n):
    mask = 10 ** 11
    tmp = n
    for i in range(n - 1):
        tmp *= n
        tmp = tmp % mask
    return tmp


def distinct_powers(i, a):
    res = set()
    rang = range(i, a + 1)
    for i in rang:
        for j in rang:
            res.add(i ** j)
    print len(res)


def digit_factorials(dn):
    import math
    d = {}

    def digits(n, d):
        f = 0
        for i in str(n):
            f += math.factorial(int(i))
        return f

    for i in range(2, 10 ** dn):
        f = digits(i, d)
        if f == i:
            print i

    for i in range(10 ** 6, 2540160):
        f = digits(i, d)
        if f == i:
            print i

def not_consequtive(a, b):
    for i in range(a + 1, b):
        if is_prime(i):
            print a, b, i
            return True
    return False


def quadratic_primes(n):
    a = range(-n, n)
    b = range(40, n)
    for j in b:
        for i in a:
            if is_prime(j):
                n = 0
                while True:
                    t = n ** 2 + n * i + j
                    n += 1
                    if t < 0:
                        break
                    if not is_prime(t):
                        # print 'np break', n-1, i, j
                        yield n - 1, i, j
                        break
                    # if n > 2:
                    #     tmp = n - 2
                    #     # 1 + 1 + 41 = 43 44 45 46
                    #     # 4 + 2 + 41 = 47
                    #     if not_consequtive((tmp ** 2 + tmp * i + j), t):
                    #         print 'nc break', n-1, i, j, (tmp ** 2 + tmp * i + j), t
                    #         yield n - 1, i, j
                    #         break


def main():

    # print not_consequtive(53, 61)
    d = {}
    for i, j, k in quadratic_primes(1000):
        # print i, j, k
        if i not in d:
            d[i] = (j, k)
    keys = d.keys()
    keys.sort()
    for k in keys:
        print k, d[k]
    # distinct_powers(2, 100)
    # print math.factorial(9) * 7
    # digit_factorials(5)
    # import math
    # for n in range(100)[1]:
    #     if math.factorial(9) * n < 10 ** n:
    #         print n
    #         break

    # print 9 ** 9
    # print self_powers(9)
    # s = 0
    # for i in range(1001)[1:]:
    #     s += self_powers(i)
    #     s = s % (10 ** 11)
    # print s
    # 4 = 3
    # print coin_sums(3)
    # 11111
    # 1112
    # 122
    # 5
    # for i in range(2800, 10000):
    #     if len(str(fib(2800))) > 1000:
    #         print i
    #         break

    # print len(fib(2800))
    # print fib(12)
    # print get_d()
    # print kst_prime(10001)

if __name__ == '__main__':
    main()
