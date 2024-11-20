from threading import Thread, Condition, current_thread as current
from collections import deque
from time import sleep
from random import random, randint

queue = deque()

class SimpleQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = deque()
        self.empty = Condition()
        self.full = Condition()


    def put(self, v):
        with self.full:
            if len(self.queue) >= self.capacity:
                self.full.wait()
        
        with self.empty:
            if len(self.queue) < self.capacity:
                self.queue.append(v)
                self.empty.notify()

    def get(self):
        with self.empty:
            if not self.queue:
                self.empty.wait()
        
        with self.full:
            v = self.queue.popleft()
            self.full.notify()
        
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
    
