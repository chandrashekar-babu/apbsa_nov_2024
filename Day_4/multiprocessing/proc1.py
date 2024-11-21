from time import sleep
from multiprocessing import Process

def foo(n):
    for i in range(n):
        print "in foo: counting ", i
        sleep(1)


def bar(n):
    for i in range(n):
        print "in bar: counting ", i
        sleep(1)


if __name__ == '__main__':
    t1 = Process(target=foo, args=(50,))
    t2 = Process(target=bar, args=(30,))

    t1.start()
    t2.start()

    for i in range(50):
        print "In main: counting", i
        sleep(1)

