from multiprocessing import Process, Array, Event
from time import sleep


arr = Array('i', range(10, 20))
squared = Event()
halved = Event()

def foo(a, s):
    for i, n in enumerate(a):
        a[i] = n*n
    s.set()

def bar(a, s, h):
    s.wait()
    print "In bar: a =", list(a)
    for i, n in enumerate(a):
        a[i] = n / 2
    h.set()



p1 = Process(target=foo, args=(arr, squared))
p2 = Process(target=bar, args=(arr, squared, halved))

p1.start()
p2.start()

halved.wait()
print "In main: arr =", list(arr)

p1.join()
p2.join()


