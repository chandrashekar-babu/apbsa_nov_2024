from threading import Thread, Lock, current_thread as current
from time import sleep
import itertools

import sys

sleep_lock = Lock()

def testfn():
    t = current()
    for i in itertools.count():
        with sleep_lock:
            print(f"{t.name}: {i=} acquired lock: sleeping")
            sleep(1)
            print(f"{t.name}: {i=} woke up")
        sleep(sys.getswitchinterval())
        

if __name__ == '__main__':
    t1 = Thread(target=testfn)
    t2 = Thread(target=testfn)
    t1.start()
    t2.start()

    t1.join()
    