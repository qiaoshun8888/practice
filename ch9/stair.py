"""
Staircase with n steps
"""


def count_steps(n):
    steps = {}
    steps[1] = 1
    steps[2] = 2
    steps[3] = 4
    for i in range(4, n + 1):
        steps[i] = steps[i - 1] + steps[i - 2] + steps[i - 3]
    return steps[n]


def main():
    print count_steps(10)

if __name__ == '__main__':
    main()
