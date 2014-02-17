
def merge(A, B):
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            # B element bigger, insert into A
            A[i + 1:] = A[i:]
            A[i] = B[j]
            j += 1
        i += 1
    if j < len(B):
        A[i + 1:] = B[j:]


if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9]
    B = [1,2,3]
    merge(A, B)
    print A
