'''
25cents. 10cents, 5 cents, 1 cents

'''


def cents(n, lte=25, sets=[25, 10, 5, 1]):
    # print n, lte
    r = 0
    sets.sort()
    for i in sets[::-1]:
        if i <= lte:
            if n > i:
                # path.append(i)
                # print i
                r += cents(n - i, lte=i, sets=sets)
            elif n == i:
                r += 1
                # print i
                # print ""
                # path.append(i)
                # print path
            else:
                r += 0
    return r

# print cents(15)
print cents(200, 200, [1, 2, 5, 10, 20, 50, 100, 200])
