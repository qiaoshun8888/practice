def permutations(s):
    if len(s) <= 1:
        return [s, ]
    c = s[-1]
    res = []
    for i in range(len(s)):
        for j in permutations(s[:-1]):
            # print i, c, j, j[:0], j[0:]
            res.append(j[:i] + c + j[i:])
    return res

if __name__ == '__main__':
    for i in permutations('test'):
        print i
