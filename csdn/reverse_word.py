'''
# 10
reverse word

don't understand the point
'''


def reverse_word(str):
    l = str.strip().split(' ')
    # for k, v in enumerate(l):
    #     l[k] = v[
    return ' '.join(l[::-1])

if __name__ == '__main__':
    test = 'i am a student.'
    print reverse_word(test)
