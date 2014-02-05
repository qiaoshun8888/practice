# coding=utf-8
"""
# 2
2 ways to do it.
    tuple
    2 stacks
"""


class Stack():

    """
    will waste space
    """
    _data = []
    _min = None

    def push(self, data):
        self._data.append((data, self._min))
        if not self._min or self._min > data:
            self._min = data
        return

    def pop(self):
        if self._data:
            tmp, self._min = self._data.pop()
            return tmp
        else:
            raise 'No more'

    def getmin(self):
        return self._min


class Stack2():

    """
    use anthor stack for min
    """
    _data = []
    _min = []

    def push(self, data):
        self._data.append(data)
        if not self._min or self._min[-1] >= data:
            self._min.append(data)

    def pop(self):
        tmp = self._data.pop()
        if tmp == self._min[-1]:
            self._min.pop()
        return tmp

    def getmin(self):
        return self._min[-1]


def main():
    s = Stack2()
    s.push(1)
    s.push(2)
    print s.getmin()
    print s.pop()
    print s.pop()
    s.push(3)
    print s.getmin()
    s.push(2)
    print s.getmin()

if __name__ == '__main__':
    main()
