"""
find all subset
"""
import copy


def subset(s):
    res = [[], ]
    while s:
        tmp = s.pop()
        # print tmp
        for i in range(len(res)):
            ii = copy.copy(res[i])
            ii.append(tmp)
            res.append(ii)
    return res


def recursive_subset(s):
    if not s:
        return [[], ]
    tmp = s.pop()
    l = recursive_subset(s)
    copy_l = copy.deepcopy(l)
    for i in copy_l:
        i.append(tmp)
    l.extend(copy_l)
    return l


if __name__ == '__main__':
    s = {1, 2, 3, 4}
    print subset(s)
    s = {1, 2, 3, 4}
    print sorted(recursive_subset(s))
