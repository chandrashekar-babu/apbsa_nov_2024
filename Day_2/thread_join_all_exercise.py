from threading import Thread, current_thread as current
from time import sleep
import random

def testfn(count, delay):
    t = current()
    for i in range(count):
        print(f"{t.name[:9]}: counting {i}/{count}")
        sleep(delay)
    print(f"{t.name} has ended.")

def joinall(threads, delay=None):
    if delay is None:
        import sys
        delay = sys.getswitchinterval()
        
    from collections import deque
    threads = deque(threads)
    while threads:
        t = threads[0]
        t.join(delay)
        if not t.is_alive():
            yield threads.popleft()
        else:
            threads.rotate(-1)

if __name__ == '__main__':
    
    counts = random.sample(range(5, 25), 10)
    workers = []
    for c in counts:
        t = Thread(target=testfn, args=(c, 1))
        t.start()
        workers.append(t)

    for t in joinall(workers, 0.1):
        print(f"Thread {t.name} finished.")


    #for t in workers:
    #    t.join()
    #    print(f"main: {t.name[:9]} finished.")

