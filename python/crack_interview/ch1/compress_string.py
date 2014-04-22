#coding=utf-8

def compress(str):
    char = str[0]
    count = 1
    res = ""
    for i in str[1:]:
        if i == char:
            count += 1
        else:
            res += "%s%d" % (char, count)
            count = 1
            char = i
    res += "%s%d" % (char, count)
    return res if len(res) < len(str) else str

if __name__ == '__main__':
    print compress("aabcccccaaa")
    print compress("aabbcc")



