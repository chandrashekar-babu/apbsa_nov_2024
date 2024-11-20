from threading import Thread, Semaphore, current_thread as current
from collections import deque
from time import sleep
from random import random, randint
from queue import Queue

queue = Queue(10)

def producer():
    t = current()
    while True:
        v = randint(10, 100)
        print(f"{t.name}: Enqueuing {v}, Queue = {list(queue.queue)}")
        queue.put(v)
        sleep(random())

def consumer():
    t = current()
    while True:
        v = queue.get()
        print(f"{t.name}: Dequeued {v}, Queue = {list(queue.queue)}")
        sleep(random() / 2)

if __name__ == '__main__':
    p = Thread(target=producer)
    c = Thread(target=consumer)
    p.start()
    c.start()
    
