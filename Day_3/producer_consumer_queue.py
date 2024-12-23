#from threading import Thread, current_thread as current
#from queue import Queue

from multiprocessing import Process as Thread, current_process as current, Queue

from time import sleep
from random import random, randint

queue = Queue(10)

def producer():
    t = current()
    while True:
        v = randint(10, 100)
        print(f"{t.name}: Enqueuing {v}")
        queue.put(v)
        sleep(random())

def consumer():
    t = current()
    while True:
        v = queue.get()
        print(f"{t.name}: Dequeued {v}")
        sleep(random())

if __name__ == '__main__':
    p = Thread(target=producer)
    c = Thread(target=consumer)
    p.start()
    c.start()
    
