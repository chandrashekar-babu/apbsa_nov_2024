from threading import Thread, Semaphore, current_thread as current
#from multiprocessing import Process as Thread, Semaphore, current_process as current
from collections import deque
from time import sleep
from random import random, randint


class SimpleQueue:
    def __init__(self, capacity=10):
        self.queue = deque()
        self.writer = Semaphore(capacity)
        self.reader = Semaphore(0)

    def put(self, v):
        self.writer.acquire()
        self.queue.append(v)
        self.reader.release()

    def get(self):
        self.reader.acquire()
        v = self.queue.popleft()
        self.writer.release()

        return v

queue = SimpleQueue(10)

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
    
