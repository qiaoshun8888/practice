'''
# 27

same as ch9, stair problem
no 3 steps
'''


def count_steps(n):
    steps = {}
    steps[1] = 1
    steps[2] = 2
    for i in range(3, n + 1):
        steps[i] = steps[i - 1] + steps[i - 2]
    return steps[n]


def main():
    print count_steps(10)

if __name__ == '__main__':
    main()
