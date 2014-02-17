def convert(d):
    def divide(d):
        x = 0
        while(not d * 10 ** x - int(d * 10 ** x) == 0):
            x += 1
        return 10 ** x

    def gcd(a, b):
        remainder = a % b
        if not remainder:
            return b
        else:
            return gcd(b, remainder)

    bottom = divide(d)
    top = d * bottom
    g = gcd(top, bottom)
    if g < 0:
        g = -g
    return '%d/%d' % (top / g, bottom / g)


def main():
    print convert(2.225)

if __name__ == '__main__':
    main()
