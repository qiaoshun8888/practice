#coding=utf-8
"""
implement a myqueue class
which implements a queue using two stacks
"""


class Myqueue():
    stack1 = []
    stack2 = []

    def push(self,data):
        self.stack1.append(data)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

def main():
    q = Myqueue()
    q.push(1)
    q.push(2)
    print q.pop()
    q.push(3)
    q.push(4)
    print q.pop()
    print q.pop()
    print q.pop()


if __name__ == '__main__':
    main()
