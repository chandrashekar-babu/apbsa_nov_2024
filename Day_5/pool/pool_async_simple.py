from multiprocessing import Pool
from time import sleep
from os import getpid


def square(x):
    print "square called on pid %d" % getpid()
    sleep(5)
    return x*x

pool = Pool(2)

print "In main: applying value 2 on process pool."
r1 = pool.apply_async(square, (2,))

print "In main: applying value 6 on process pool."
r2 = pool.apply_async(square, (6,))

print "Sleeping for 7 seconds..."
sleep(7)
print "Woke up..."
print "Result of r1 (2) = ", r1.get()
print "Result of r2 (6) = ", r2.get()

print r1
print r2
