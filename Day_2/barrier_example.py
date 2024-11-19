from threading import Thread, Barrier, current_thread as current
from time import sleep
import random

def testfn(delay):
    t = current()
    print(f"[{t.name}]: sleeping for {delay} seconds")
    sleep(delay)
    print(f"[{t.name}]: woke up!")
    others.wait()
    print(f"[{t.name}]: continuing!")

if __name__ == '__main__':
    NUM_THREADS = 5
    workers = []
    delays = random.sample(range(5, 30, 5), NUM_THREADS)
    others = Barrier(NUM_THREADS)
    for d in delays:
        t = Thread(target=testfn, args=(d,))
        t.start()
        workers.append(t)
    
    for t in workers:
        t.join()

