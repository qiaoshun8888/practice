'''
1. recursive # done that before
2. bit masks!!!
'''
import copy


def recurisve_subsets(array):
    if array:
        last = array.pop()
        rest = recurisve_subsets(array)
        tmp = copy.deepcopy(rest)
        for t in tmp:
            t.append(last)
        rest.extend(tmp)
        return rest
    else:
        return [[]]


def subsets(array):
    length = len(array)
    for i in range((1 << length)):
        # print bin(i)
        subset = []
        for k, j in enumerate(bin(i)[2:][::-1]):
            if j == '1':
                subset.append(array[k])
        print subset


if __name__ == '__main__':
    print recurisve_subsets([1, 2, 3])
