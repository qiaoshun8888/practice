import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from euler import is_prime


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


def main():
    d = {}
    for i, j, k in quadratic_primes(1000):
        # print i, j, k
        if i not in d:
            d[i] = (j, k)
    keys = d.keys()
    keys.sort()
    best = 0
    best_d = None
    for k in keys:
        if k > best:
            best = k
            best_d = d[k]
    print best_d[0] * best_d[1]

if __name__ == '__main__':
    main()
