def self_power(n):
    mask = 10 ** 10
    tmp = n
    for i in range(n - 1):
        tmp *= n
        tmp = tmp % mask
    return tmp


def self_powers(n):
    mask = 10 ** 10
    tmp = 0
    for i in range(1, n + 1):
        tmp += self_power(i)
        tmp = tmp % mask
    return tmp

if __name__ == '__main__':
    print self_powers(1000)
