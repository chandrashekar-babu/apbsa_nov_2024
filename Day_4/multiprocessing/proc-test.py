import os
from time import sleep
from multiprocessing import Process

def foo():
   for i in range(10):
       print "In foo: counting", i
       sleep(1)


def bar():
   for i in range(10):
       print "In bar: counting", i
       sleep(1)

p1 = Process(target=foo)
p2 = Process(target=bar)
p1.start()
p2.start()

#foo()
#bar()




        


