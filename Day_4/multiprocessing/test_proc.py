from multiprocessing import Process
from time import sleep

def foo():
    for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10: 
        print "In foo: counting", i
        sleep(1)

def bar():
    for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10: 
        print "In bar: counting", i
        sleep(1)

if __name__ == '__main__':
    t1 = Process(target=foo)
    t2 = Process(target=bar)

    #t1.daemon = True
    #t2.daemon = True

    t1.start()
    t2.start()

    for i in range(5):
        print "In main: counting", i
        sleep(1)

    t1.join()
    t2.join()

    print "Main thread complete."



