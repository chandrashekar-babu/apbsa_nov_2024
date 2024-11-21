from multiprocess import Process
from time import sleep

def foo(name):
    for i in range(10):
        print("{} counting {}".format(name, i))
        sleep(1)
        exit(1)


if __name__ == '__main__':
    workers = {}

    for i in range(20):
        workers[i] = Process(target=foo, args=("worker-{}".format(i),))
        workers[i].start()

    for i in range(20):
        workers[i].join()


