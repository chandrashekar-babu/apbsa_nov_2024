from multiprocessing import Pool
from time import sleep
from os import getpid


def square(x):
    print "square called on pid %d" % getpid()
    sleep(5)
    return x*x

#pool = Pool(8)
pool = {}
from multiprocessing import Queue
jobq = Queue(8)
resultq = Queue(8)
def handle_work():
    while True:
        fn, args = jobq.get()
        resultq.put(fn(*args))

for i in range(8):
    pool[i] = Process(target=handle_work, args=(jobq,))
    pool[i].start()

print "In main: applying value 2 on process pool."
#r1 = pool.apply_async(square, (2,))

def apply_async(fn, args):
    jobq.put((fn, args))


print "In main: applying value 6 on process pool."
r2 = pool.apply_async(square, (6,))

print "Result of r1 (2) = ", r1.get()
print "Result of r2 (6) = ", r2.get()

