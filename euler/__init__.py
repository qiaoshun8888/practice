import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import math


def is_prime(n):
    for i in range(int(math.sqrt(n)) + 1)[2:]:
        if n % i == 0:
            return False
    return True
