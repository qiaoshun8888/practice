import math


def is_prime(n):
    for i in range(int(math.sqrt(n)) + 1)[2:]:
        if n % i == 0:
            return False
    return True


def kst_prime(k):
    i = 0
    while True:
        i += 1
        if is_prime(i):
            k -= 1
            if k < 0:
                return i

if __name__ == '__main__':
    print kst_prime(10001)
