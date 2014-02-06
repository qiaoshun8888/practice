import copy


def longest(s):
    '''
    this is a wrong solution
    O(n ** 2) should be correct
    '''
    stack1 = []
    stack2 = None
    for i in s:
        if not stack2:
            print ""
            if len(stack1) > 1:
                if i == stack1[-1]:
                    stack2 = copy.deepcopy(stack1)
            if len(stack1) > 2:
                if i == stack1[-2]:
                    stack2 = copy.deepcopy(stack1)
        if stack2:
            if i == stack2.pop():
                print i,
            else:
                print ""
                stack2 = None
        stack1.append(i)


if __name__ == '__main__':
    longest('11112332112332111')
