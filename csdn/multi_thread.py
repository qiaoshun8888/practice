import time
from threading import Thread


queue = []


class Dispatcher(Thread):

    def run(self):
        global queue
        while True:
            task = raw_input('task')
            queue.append('%s, %s' % (task, str(time.time())))


class Worker(Thread):

    def run(self):
        global queue
        while True:
            if queue:
                print 'get ' + queue.pop(0) + ' \n'
            time.sleep(1)


def main():
    d = Dispatcher()
    d.start()

    w = Worker()
    w.start()


if __name__ == '__main__':
    main()
