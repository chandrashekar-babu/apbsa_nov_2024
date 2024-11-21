from time import sleep
from threading import Thread

def foo():
    i = 0
    while True:
        print "in foo: counting ", i
        i += 1

p1 = Thread(target=foo)
p2 = Thread(target=foo)

p1.start()
p2.start()

