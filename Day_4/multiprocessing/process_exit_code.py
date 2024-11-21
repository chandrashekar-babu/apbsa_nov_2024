from multiprocess import Process
from time import sleep

def foo(name):
    from multiprocessing import current_process
    p = current_process()
    for i in range(20):
        print("{}[{}]: counting {}".format(p.name, p.pid, i))
        sleep(1)
    exit(6)


if __name__ == '__main__':
    p = Process(target=foo, name="worker", args=("worker",))
    p.start()
    print("Process started: pid =", p.pid)
    sleep(3)
    p.terminate()
    p.join()
    print(p.exitcode)

