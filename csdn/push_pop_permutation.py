'''
# 29

push = [1, 2, 3, 4, 5]
pop maybe [4, 5, 3, 2, 1]
get all pop possiblity

like () problem, maybe recursive?

I worte bullshit...Sleepy
'''
import copy


def all(array):
    '''dfs'''
    l = len(array)
    stack = []
    stack.append({'path': ['push'], 'push': 1, 'pop': 0})
    while stack:
        node = stack.pop()
        if node['push'] > node['pop'] and node['pop'] < l:
            '''can pop'''
            tmp = copy.deepcopy(node)
            tmp['path'].append('pop')
            tmp['pop'] += 1
            stack.append(tmp)
            del tmp
        if node['push'] < l:
            '''can push'''
            tmp = copy.deepcopy(node)
            tmp['path'].append('push')
            tmp['push'] += 1
            stack.append(tmp)
            del tmp
        if node['push'] == l and node['pop'] == l:
            yield node['path']
        del node

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    for i in all(a):
        t = copy.deepcopy(a)
        s = []
        for j in i:
            if j == 'push':
                s.append(t.pop(0))
            if j == 'pop':
                print s.pop(),
        print ''
