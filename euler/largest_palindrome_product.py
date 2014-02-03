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


if __name__ == '__main__':
    best = float('-inf')
    best_ij = (0, 0)
    for i, j, s in big_palindrome():
        if int(s) > best:
            best_ij = (i, j)
            best = int(s)
    print best
