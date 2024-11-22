from multiprocessing import Pool, Queue
from time import sleep, time
from os import getpid

CAPACITY = 8

workers = Pool(CAPACITY)
queue = Queue(CAPACITY)
result = Queue(CAPACITY)

def handle_work(work, inbox, output):
    while True:
        print "Worker %d waiting for input..." % getpid()
        data = inbox.get()
        print "Worker %d got input: %d" % (getpid(), data)
        result = work(data)
        print "Worker %d computed %d" % (getpid(), result)
        outbox.put(result)
        
def square(x):
    sleep(0.5)
    return x*x


print "Main: initializing workers..."
workers.apply_async(square, (10,))


for i in range(10):
    print "Main: assigning %d to workers..." % i
    queue.put(i)
    print "Main: awaiting result..."
    r = result.get()
    print "Main: result =", r.get()


