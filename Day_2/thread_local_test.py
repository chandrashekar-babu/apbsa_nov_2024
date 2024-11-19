from threading import Thread
import threading
from time import sleep

class Local: pass

a = threading.local()
#a = Local()
a.data = 100

def foo():
    a.data = 500
    print(f"In foo: {a.data=}")
    sleep(2)
    print(f"In foo: a now is {a.data}")

def bar():
    a.data = 200
    print(f"In bar: {a.data=}")
    sleep(1)
    print(f"In bar: a now is {a.data}")

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)
    t1.start()
    t2.start()
    print("In main: a =", a.data)
    t1.join()
    t2.join()
    print("In main: a =", a.data)
