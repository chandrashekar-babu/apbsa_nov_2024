#from threading import Thread, Event
from multiprocessing import Process as Thread, Event

from time import sleep

class Value:
    def __init__(self, v):
        self.__dict__['contents'] = {'value': v}
        self.__dict__['updated'] = Event()
        self.__dict__['updated'].set()

    def __setattr__(self, attr, value):
        self.__dict__['contents'][attr] = value
        self.__dict__['updated'].set()

    def __getattr__(self, attr):
        self.__dict__['updated'].wait()
        v = self.__dict__['contents'][attr]
        self.__dict__['updated'].clear()
        return v

if __name__ == '__main__':
    num = Value(100)

    def foo(n):
        print("In foo: v = ", n.value)
        n.value = 500
        sleep(1)
        print("In foo: v = ", n.value)


    def bar(n):
        print("In bar: v =", n.value)
        n.value = 100
        sleep(1)
        print("In bar: v now is", n.value)



    foo_thread = Thread(target=foo, args=(num,))
    bar_thread = Thread(target=bar, args=(num,))

    foo_thread.start()
    bar_thread.start()

