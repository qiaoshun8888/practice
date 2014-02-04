
def distinct_powers(i, a):
    res = set()
    rang = range(i, a + 1)
    for i in rang:
        for j in rang:
            res.add(i ** j)
    return len(res)

if __name__ == '__main__':
    print distinct_powers(2, 100)
