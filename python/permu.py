import copy


def test(s):
    res = []
    stack1 = []
    stack2 = None
    for i in s:
        stack1.append(i)
        if ((len(stack1) >= 2 and i == stack1[-2]) or (len(stack1) >= 3 and i == stack1[-3])):
            if stack2 == None:
                stack2 = copy.copy(stack1)
                print len(stack1)
                stack2.pop()
                # print stack1, i
                if i == stack1[-2]:
                    print (stack2.pop()), 'get'
                    # res.append(stack2.pop())
                elif i == stack1[-3]:
                    print (stack2.pop()), 'get'
                    print (stack2.pop()), 'get'
                    # res.append(stack2.pop())
                    # res.append(stack2.pop())
        elif (stack2 and i == stack2[-1]):
            print (stack2.pop()), 'get'
            # res.append(stack2.pop())
        else:

            stack2 = None
            yield res


def main():
    for i in test('abccccba'):
        print i, 'res'


if __name__ == '__main__':
    main()
