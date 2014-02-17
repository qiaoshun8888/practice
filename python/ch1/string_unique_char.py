#coding=utf-8

def unique(str):
    for i, c in enumerate(str):
        if c in str[:i]:
            return False
    return True

if __name__ == '__main__':
    print unique("abc")
    print unique("abcbabc")
