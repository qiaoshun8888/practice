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


def big_palindrome():
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            s = str(i * j)
            ok = False
            for k in range(len(s) / 2):
                if not s[k] == s[len(s) - 1 - k]:
                    ok = False
                    break
                ok = True
            if ok:
                yield i, j, s


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


def sum_square_difference(n):
    s1 = 0
    s2 = 0
    for i in range(n + 1):
        s1 += i ** 2
        s2 += i
    s2 = s2 ** 2
    return s2 - s1


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


def factorial_digit_sum(n):
    # f = math.factorial(n)
    f = 1
    for i in range(n + 1)[1:]:
        f *= i

    s = 0
    for i in str(f):
        s += int(i)
    return s


def fib(n):
    f = {}
    for i in range(n + 1)[1:]:
        if i <= 2:
            f[i] = 1
        else:
            f[i] = f[i - 1] + f[i - 2]
    return f[n]


def maximum_path_sum(t):
    import copy
    from structs import btree

    if not t:
        t = [[3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3]]
    if t:
        t = t.split('\n')
        for k, v in enumerate(t):
            t[k] = [int(i) for i in v.strip().split(' ')]

    for i, r in enumerate(t[::-1]):
        for k, v in enumerate(r):
            r[k] = btree.Node(v)
            if i > 0:
                r[k].left = t[-i][k]
                r[k].right = t[-i][k + 1]

    def path_sums():
        root = t[0][0]
        stack = []
        stack.append((root, 0, []))
        while stack:
            e, res, path = stack.pop()
            tmppath = copy.copy(path)
            tmppath.append(e.data)
            if e.left:
                stack.append((e.left, res + e.data, tmppath))
            if e.right:
                stack.append((e.right, res + e.data, tmppath))
            if not e.left and not e.right:
                # leaf
                yield res + e.data, tmppath

    best = 0
    best_path = []
    for i, j in path_sums():
        if i > best:
            best = i
            best_path = j
    return best, best_path
# def k_digit_fib(k):


def main():
    # for i in range(2800, 10000):
    #     if len(str(fib(2800))) > 1000:
    #         print i
    #         break
#     print maximum_path_sum("""75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""")
    # print len(fib(2800))
    # print fib(12)
    # print get_d()
    # print kst_prime(10001)

if __name__ == '__main__':
    main()
