def g(array):
    current = 0
    best = float('-inf')
    start = 0
    end = 0
    best_se = None
    for k, i in enumerate(array):
        current += i
        if current < 0:
            start = k + 1
            current = 0
        if current > best:
            end = k
            best_se = (start, end)
            best = current
    return best, best_se

if __name__ == '__main__':
    print g([-1, 2, 3, 5, -2])
