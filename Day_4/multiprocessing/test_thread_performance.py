#from threading import Thread
from multiprocessing import Process as Thread
from time import time

def foo():
    a = range(5000)
    for i, v in enumerate(a):
        a[i] **= a[i]


threads = { }


start = time()

for i in range(16):
    threads[i] = Thread(target=foo)
    threads[i].start()

for t in threads.values(): t.join()

end = time()

print "Duration:", end - start


