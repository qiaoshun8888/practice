import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from euler import is_prime


def kst_prime(k):
    i = 0
    while True:
        i += 1
        if is_prime(i):
            k -= 1
            if k < 0:
                return i

if __name__ == '__main__':
    print kst_prime(10001)
