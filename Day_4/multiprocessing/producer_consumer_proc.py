from multiprocessing import Process
from random import randint, random
from time import sleep
from multiprocessing import Queue


queue = Queue(10)

def producer():
    while True:
        v = randint(10, 100)
        queue.put(v)
        print "Producer: {0}".format(v)
        sleep(random()/2)


def consumer():
    while True:
        v = queue.get()
        print "Consumed: {0}".format(v)
        sleep(random())

p = Process(target=producer)
c = Process(target=consumer)

p.start()
c.start()


