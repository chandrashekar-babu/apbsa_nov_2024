from multiprocessing import Process, current_process as current, Queue

from time import sleep
from random import random, randint

def producer(q):
    t = current()
    while True:
        v = randint(10, 100)
        print(f"{t.name}: Enqueuing {v}")
        q.put(v)
        sleep(random())

def consumer(q):
    t = current()
    while True:
        v = q.get()
        print(f"{t.name}: Dequeued {v}")
        sleep(random())

if __name__ == '__main__':
    queue = Queue(10)

    p = Process(target=producer, args=(queue,))
    c = Process(target=consumer, args=(queue,))
    p.start()
    c.start()
    
