# coding=utf-8
"""
No good at all
"""


def biggest_seq(l):
    if len(l) == 1:
        return l[0], 0, 0, 0

    res, start, end, afterend = biggest_seq(l[:-1])

    if l[-1] > res:
        end = len(l) - 1
        if res + afterend <= 0:
            start = end
            res = l[-1]
        else:
            res = l[-1] + res + afterend
        afterend = 0
    else:
        if l[-1] + afterend <= 0:
            afterend += l[-1]
        else:
            end = len(l) - 1
            afterend = 0
            res = l[-1] + res + afterend
    return res, start, end, afterend


def main():
    print biggest_seq([1, -2, 3, 10, -4, 7, 2, -5])

if __name__ == '__main__':
    main()
