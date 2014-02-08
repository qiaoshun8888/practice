class Solution:
    # @return an integer

    def reverse(self, x):
        ''' extra n space '''
        neg = False
        if x < 0:
            neg = True
            x = -x
        r = int(str(x)[::-1])
        return r if not neg else -r

    def reverse_inplace(self, x):
        def get_length(x):
            k = 1
            while 10 ** k <= x:
                k += 1
            return k
        # print get_length(x)

        def get_digit(x, d):
            return x % 10 ** (d + 1) / 10 ** (d)

        def set_digit(x, d, v):
            return (x % 10 ** d) + v * 10 ** d

        # print get_digit(x, 0)
        # print get_digit(x, 1)
        # print get_digit(x, 2)
        # print set_digit(x, 2, 5)
        # print x


if __name__ == '__main__':
    s = Solution()
    print s.reverse_inplace(123)
