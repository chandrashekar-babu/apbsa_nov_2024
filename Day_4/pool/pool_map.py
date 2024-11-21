from multiprocessing import Pool
from os import getpid

def square(x):
    print "Squaring {} on process (pid = {})".format(x, getpid())
    return x*x

data = range(10, 32)

p = Pool(4)

print "Starting parallel map..."
result = p.map(square, data)

print data
print result

