from threading import Thread, Condition, current_thread as current
from collections import deque
from time import sleep
from random import random, randint

queue = deque()

def producer():
    t = current()
    while True:
        v = randint(10, 100)
        print(f"{t.name}: Enqueuing {v}")
        queue.append(v)
        sleep(random())

def consumer():
    t = current()
    while True:
        v = queue.popleft()
        print(f"{t.name}: Dequeued {v}")
        sleep(random())

if __name__ == '__main__':
    p = Thread(target=producer)
    c = Thread(target=consumer)
    p.start()
    c.start()
    
