d = {}


def _coin_sums(n, circulation, lte):
    global d
    if '%s: %s' % (n, lte) in d:
        return d['%s: %s' % (n, lte)]
    '''
    circulation must be reverse sorted
    '''
    r = 0
    for i in circulation:
        if i <= lte:
            if n == i:
                r += 1
            elif n > i:
                r += _coin_sums(n - i, circulation, i)
            else:
                r += 0
    d['%s: %s' % (n, lte)] = r
    return r


def coin_sums(n):
    circulation = [1, 2, 5, 10, 20, 50, 100, 200][::-1]
    lte = 200
    n = 200
    return _coin_sums(n, circulation, lte)


def main():
    print coin_sums(200)

if __name__ == '__main__':
    main()
