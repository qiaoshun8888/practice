'''
# 30
stupid solution
there should be a better way
'''

# n = 12
#


def range_1s(n):
    t = 1
    m = n
    while n > 1:
        t += 1
        n /= 10

    c = 0
    for i in range(1, m + 1):
        for j in range(t):
            if i % 10 ** (j + 1) / 10 ** j == 1:
                c += 1
    print c

if __name__ == '__main__':
    range_1s(1001)
