from multiprocessing import Process
from time import sleep
import os

def child_handler():
   for i in range(30):
       print "In child[%d]: counting %d" % (os.getpid(), i)
       sleep(1)

procs = { }
for i in range(5):
    procs[i] = Process(target=child_handler)
    procs[i].start()

sleep(15)
print "Main program exited."

        



