import os
from time import sleep
from multiprocessing import Process

class Task:
    def __init__(self):
       self.i = 0

    def foo(self):
       for i in range(10):
           print "In foo: counting", self.i
           self.i += 1
           sleep(1)


    def bar(self):
       for i in range(10):
           print "In bar: counting", self.i
           self.i += 1
           sleep(1)

t = Task()

#t.foo()
#t.bar()

p1 = Process(target=t.foo)
p2 = Process(target=t.bar)
p1.start()
p2.start()

#foo()
#bar()




        


