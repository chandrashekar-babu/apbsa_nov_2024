from time import sleep
#from multiprocessing import Process
from threading import Thread as Process

i = 0

def foo(name):
    global i
    while True:
        print(f"In foo[{name}]: counting {i}")
        sleep(0.5)
        i += 1

p1 = Process(target=foo, args=("process-1",))
p2 = Process(target=foo, args=("process-2",))

p1.start()
p2.start()

