"""
done several times
"""

COINSET = [1, 2, 5, 10, 20, 50, 100, 200]


def coins(n):
    def helper(n, lte, path):
        for i in COINSET[::-1]:
            if i <= lte:
                path.append(i)
                if i == n:
                    yield path
                elif i < n:
                    for j in helper(n - i, i, path):
                        yield j
                path.pop()
    COINSET.sort()
    return helper(n, COINSET[-1], [])


def coins_number(n):
    def helper(n, lte):
        c = 0
        for i in COINSET[::-1]:
            if i <= lte:
                if i == n:
                    c += 1
                elif i < n:
                    c += helper(n - i, i)
        return c
    COINSET.sort()
    return helper(n, COINSET[-1])

if __name__ == '__main__':
    c = coins_number(200)
    print c
