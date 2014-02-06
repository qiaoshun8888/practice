#coding=utf-8

def space_encode(string, true_length):
    string = list(string)
    spaces = []
    for i in range(true_length):
        if string[i] == ' ':
            spaces.append(i)
    last_index = true_length
    n = len(spaces)
    for i in (spaces[::-1]):
        string[i+n*2+1:last_index+n*2] = string[i+1:last_index]
        string[i+2*n-2:i+2*n+1] = ['%','2','0']
        n -= 1
        last_index = i
    print string

if __name__ == '__main__':
    space_encode('hello world python    ', 18)

