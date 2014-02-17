

def powerful_digit_sum(m, n):
    r = m ** n
    res = 0
    for i in str(r):
        res += int(i)
    return res

if __name__ == '__main__':
    best = 0
    best_ij = None
    for i in range(2, 100):
        for j in range(2, 100):
            r = powerful_digit_sum(i, j)
            if r > best:
                best = r
                best_ij = (i, j)
    print best, best_ij
