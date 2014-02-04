'''
with bugs
don't wanna fix it for now
useless.
'''

def smallest(n):
    n_list = list(bin(n)[2:])
    i0 = n_list[::-1].index('0')
    i1 = n_list.index('1')
    if i0 > -1 and i1 > -1:
        n_list[i0], n_list[i1] = n_list[i1], n_list[i0]
        return n_list
    else:
        return bin(n)


def largest(n):
    n_list = list(bin(n)[2:])
    i0 = n_list.index('0')
    i1 = n_list[::-1].index('1')
    if i0 > -1 and i1 > -1:
        n_list[i0], n_list[i1] = n_list[i1], n_list[i0]
        return n_list
    else:
        return bin(n)


def main():
    n =6
    print smallest(n)
    print largest(n)


if __name__ == '__main__':
    main()
