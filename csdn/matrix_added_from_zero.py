'''
# 45
no clear answer
I think it's not that hard
  b
a e c
  d

e = a + b + c + d
O(n ** 2)
'''


def is_added_from_zero(matrix):
    '''
    psudocode
    '''
    for i in m:
        for j in n:
            e = matrix[i][j]
            s = 0
            if i > 1:
                s += matix[i - 1][j]
            if i < m:
                s += matix[i + 1][j]
            if j > 1:
                s += matix[i][j - 1]
            if j < n:
                s += matix[i][j + 1]
            if not e == s:
                return False
    return True
