'''
# 17

find the first char that only shows once in a string
'''


def find1(s):
    '''
    brutal, O(n), extra space O(n)
    '''
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in s:
        if d[i] == 1:
            return i
    return -1


def find2(s):
    '''
    in place no extra space, O(n **2) time
    '''
    for k, v in enumerate(s):
        dup = False
        for sk, sv in enumerate(s):
            if not sk == k and sv == v:
                dup = True
                break
        if not dup:
            return v
    return -1


def main():
    test = 'abaccdeff'
    print find1(test)
    print find2(test)

if __name__ == '__main__':
    main()
