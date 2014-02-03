# coding=utf-8
"""
Danger!!!!
"""


class Stack():
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


def main():
    s = Stack()
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
