"""
find the probability of collision with n ants
on  n-vertex polygon
"""


def probability(n):
    return float(2) / 2 ** n


def main():
    print probability(3)
    print probability(4)
    print probability(5)

if __name__ == '__main__':
    main()
