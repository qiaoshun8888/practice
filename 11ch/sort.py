
import copy

dic1 = {}
for c in "abcdefghijklmnopqrstufwxyz":
    dic1[c] = 0


def v(str1):
    global dic1
    dic2 = copy.copy(dic1)

    res = ""
    for i in str1:
        if i.lower() in dic2:
            dic2[i.lower()] += 1
    for c in "abcdefghijklmnopqrstufwxyz":
        if dic2[c] > 0:
            res += c + str(dic2[c])

    return res


def sort_for_anagrams(A):
    dic1 = {}
    for i in A:
        if v(i) in dic1:
            dic1[v(i)] .append(i)
        else:
            dic1[v(i)] = [i]
    res = []
    for i in dic1.values():
        res.extend(i)
    return res

if __name__ == '__main__':
    A = ['hahah', 'cccddd', 'aahhh', 'dcdcdc']
    print sort_for_anagrams(A)
