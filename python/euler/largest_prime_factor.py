import math


def is_good(n):
    for i in range(int(math.sqrt(n)))[::-1]:
        if i > 1 and n % i == 0:
            return False
    return True


def big_prime():

    for i in range(775146)[::-2]:
        if i > 0 and 600851475143 % i == 0:
            if i % 3 and i % 5 and i % 7 and i % 11:
                if is_good(i):
                    print i


if __name__ == '__main__':
    big_prime()
