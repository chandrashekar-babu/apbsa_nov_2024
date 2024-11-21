from multiprocessing import Process, Condition
from time import sleep

def foo(c):
    with c:
        print "In foo: waiting on condition..."
        c.wait()

    print "In foo: woke up on condition..."


def bar(c):
    print "In bar: sleeping for 5 seconds..."
    sleep(5)
    with c:
        print "In bar: notifying condition..."
        c.notify()
    
    print "In bar: complete..."


condition = Condition()
f = Process(target=foo, args=(condition,))
b = Process(target=bar, args=(condition,))

f.start()
b.start()


