

def origin_rod_cutting(p, n):
    r = [None] * (n + 1)
    r[0] = 0
    for j in range(n):
        q = float('-inf')
        for i in range(j + 1):
            q = max(q, p[i] + r[j - i])
        r[j + 1] = q
    return r[n]


def modified_rod_cutting(p, c, n):
    r = [None] * (n + 1)
    r[0] = 0
    for j in range(n):
        q = float('-inf')
        for i in range(j):
            q = max(q, p[i] + r[j - i] - c[i])
        q = max(q, p[j] + r[0])
        r[j + 1] = q
    return r[n]

if __name__ == '__main__':
    p = [0, 10, 1, 0]
    c = [0, 20, 0]
    n = 4
    print origin_rod_cutting(p, n)
    print modified_rod_cutting(p, c, n)
