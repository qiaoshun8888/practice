import math


def fib(n):
    f = {}
    for i in range(n + 1)[1:]:
        if i <= 2:
            f[i] = 1
        else:
            f[i] = f[i - 1] + f[i - 2]
    return f[n]



def main():
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
