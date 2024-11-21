from multiprocessing import Process
from mmap import mmap
from time import sleep

def foo(m):
    m.write("Hello world\n")


def bar(m):
    sleep(1)
    print "In bar: m =", m.readline()


m = mmap(-1, 100)

p1 = Process(target=foo, args=(m,))
p2 = Process(target=bar, args=(m,))

p1.start()
p2.start()

