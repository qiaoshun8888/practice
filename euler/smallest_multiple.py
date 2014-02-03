import math


def get_d(n):
    r = {}
    for i in range(int(math.sqrt(n)) + 1)[2:]:
        if n % i == 0:
            r[i] = 1
            if i == n / i:
                r[i] += 1
            for k, v in get_d(n / i).items():
                if k in r:
                    r[k] += v
                else:
                    r[k] = v
            break
    # if 1 in r:
    #     r[1] += 1
    # else:
    #     r[1] = 1
    # if n in r:
    #     r[n] += 1
    # else:
    #     r[n] = 1
    return r


def smallest_multiple(n):
    r = {}
    for i in range(n + 1)[1:]:
        d = get_d(i)
        if d:
            for k, v in d.items():
                if k in r:
                    r[k] = max(r[k], d[k])
                else:
                    r[k] = d[k]
        else:
            r[i] = 1
    s = 1
    for k in r:
        for i in range(r[k]):
            s *= k
    # print r
    # for i in r:
    #     s *= i

    return s


if __name__ == '__main__':
    print smallest_multiple(20)
