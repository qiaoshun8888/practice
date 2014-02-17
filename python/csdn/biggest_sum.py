# coding=utf-8
"""
# 3
if you have time,
try recursive, should work too.
"""


def biggest_seq1(l):
    current = 0
    best = float('-inf')
    for i in l:
        current += i
        if current > best:
            best = current
        if current < 0:
            current = 0
    return best


def main():
    print biggest_seq([1, -2, 3, 10, -4, 7, 2, -5])

if __name__ == '__main__':
    main()
