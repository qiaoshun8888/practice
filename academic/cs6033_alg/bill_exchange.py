# coding=utf-8
"""
What is the optimal solution for 379 dollars on {1;5;10;20;50;100}
3 * 100 + 50 + 20 + 5 + 4 * 1

What if it's [1, 5, 10, 20, 50, 94, 100]
We got 3 * 100 + 50 + 20 + 5 + 4 * 1 by alg
But actually should be 4 * 94 + 3 * 1


"""

def main(target, S):
    result = []
    for i in sorted(S)[::-1]:
        result.append((target / i, i))
        target = target % i
    return result

if __name__ == '__main__':
    print main(379, [1, 5, 10, 20, 50, 100])
