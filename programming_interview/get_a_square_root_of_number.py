def sqrt(n):
    def sqrt_helper(start, end, step):
        # print start, end, step
        if step < .000001:
            return start, end, step

        for i in range(10):
            r = (start + i * step)
            if r ** 2 == n:
                return r, r, 0
            elif r ** 2 > n:
                return sqrt_helper(r - step, r, step / 10)
    return sqrt_helper(0, n, float(1))[0]


def main():
    print sqrt(2)

if __name__ == '__main__':
    main()
