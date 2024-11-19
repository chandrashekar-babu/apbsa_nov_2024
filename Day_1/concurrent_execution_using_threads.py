from gevent import monkey
monkey.patch_all()

from threading import Thread
import time

def foo():
    for i in range(10):
        print(f"foo: counting {i}")
        time.sleep(1)        

def bar():
    for i in range(10):
        print(f"bar: counting {i}")
        time.sleep(1)

def main():
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)
    print(t1, t2)
    t1.start()
    t2.start()
    print("Threads started, waiting for them to complete")
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()

    
        