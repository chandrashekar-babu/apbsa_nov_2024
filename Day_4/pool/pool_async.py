from multiprocessing import Pool
from time import sleep, time

def square(x):
    sleep(0.5)
    return x*x

data = range(10) 

pool = Pool(4)

print "Main: starting computation..."
work = [ pool.apply_async(square, (i,)) for i in data ]
print "Main: work =", work

for i in range(3): 
    print "Main: i =", i
    sleep(0.5)

print "Main: now waiting for the result..."
result = [ w.get() for w in work ]
print "Main: result =", result

