from multiprocessing import Process as Task
from multiprocessing import Value

#from threading import Thread as Task
from time import sleep


#class Value:
#    def __init__(self, ctype, value):
#        self.value = value


def foo(n):
    print("In foo: v = ", n.value)
    sleep(1)
    n.value = 500
    print("In foo: v now is", n.value)


def bar(n):
    print("In bar: v =", n.value)
    sleep(2)
    print("In bar: v now is", n.value)


if __name__ == '__main__':
    num = Value("i", 100)

    t1 = Task(target=foo, args=(num,))
    t2 = Task(target=bar, args=(num,))

    t1.start()
    t2.start()
    print(f"Created tasks - {t1} and {t2}")