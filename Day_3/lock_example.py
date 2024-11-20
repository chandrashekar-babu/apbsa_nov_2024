from threading import Thread, Lock
from time import sleep
from random import random

SIZE = 10

nums = list(range(SIZE))
nums_lock = Lock()

result1 = []
result2 = []

def pick_elements(data, howmany, result):
    for i in range(howmany):
        with nums_lock:
            v = data[0]
            sleep(random())
            del data[0]
            result.append(v)
            sleep(random())

def pick_elements_buggy(data, howmany, result):
    for i in range(howmany):
        nums_lock.acquire()
        v = data[0]
        sleep(random())
        del data[0]
        result.append(v)
        sleep(random())
        nums_lock.release()

def pick_elements_legacy(data, howmany, result):
    for i in range(howmany):
        try:
            nums_lock.acquire()
            v = data[0]
            sleep(random())
            del data[0]
            result.append(v)
            sleep(random())
        finally:
            nums_lock.release()



if __name__ == '__main__':
    t1 = Thread(target=pick_elements, args=(nums, SIZE // 2, result1))
    t2 = Thread(target=pick_elements, args=(nums, SIZE // 2, result2))
    t1.start()
    t2.start()
    print("Threads started, waiting for them to finish.")
    t1.join()
    t2.join()
    print(f"{nums=}")
    print("Common items in results: ", set(result1) & set(result2))   