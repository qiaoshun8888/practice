# coding=utf-8


def reverse(A, start, end):
    # for reverse in place
    n = end - start
    for i in range(n / 2):
        A[start + i], A[end - 1 - i] = A[end - 1 - i], A[start + i]


def reverse_word(A):
    '''
    for John
    '''
    reverse(A, 0, len(A))
    last_space = 0
    for i in range(len(A)):
        if A[i] == ' ':
            reverse(A, last_space, i)
            last_space = i + 1
    reverse(A, last_space, len(A))

if __name__ == '__main__':
    # python string is imutable. has to convert to list
    test = "test reverse function"
    test = list(test)
    reverse_word(test)
    print ''.join(test)
