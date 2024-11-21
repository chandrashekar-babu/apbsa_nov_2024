from multiprocessing import Process
from time import sleep

def foo():
    for i in range(5):
        print "Foo: counting", i
        sleep(1)

def bar():
    for i in range(5):
        print "Bar: counting", i
        sleep(1)

t1 = Process(target=foo)
t2 = Process(target=bar)

t1.start()
t2.start()

t1.join()
print "Thread 1 finished"

t2.join()
print "Thread 2 finished"

print "Main finished"

#foo()
#bar()
