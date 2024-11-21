from multiprocessing import Pool
from time import sleep, time

def square(x):
    #sleep(0.5)
    y = 0
    for i in xrange(10000):
        for j in xrange(1000):
           y += i * j
    return x*x

data = range(32)

p = Pool(64)

#print "Starting  map..."
#start = time()
#result = map(square, data)
#print "Result: ", result, "Time: ", time() - start

print "Starting parallel map..."
start = time()
result = p.map(square, data)
print "Result: ", result, "Time: ", time() - start


