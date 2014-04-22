def binary_string(n):
    if n >= 1 or n <= 0:
        return 'error'

    current = 0
    res = ""
    for i in range(32):
        # print res
        current += .5 ** (i + 1)
        if current > n:
            res += "0"
            current -= .5 ** (i + 1)
        elif current < n:
            res += "1"
        else:
            res += "1"
            break
    if current == n:
        return '.' + res
    else:
        return 'error'

if __name__ == '__main__':
    print binary_string(.72)
