from threading import Thread
import time

def foo():
    print("this is foo...")

def bar():
    print("this is bar...")

class RunPeriodic:
    pass # TODO

def main():
    t1 = RunPeriodic(target=foo, delay=2)
    t2 = RunPeriodic(target=bar, delay=1)
    print(t1, t2)
    t1.start()
    t2.start()
    time.sleep(10)
    t1.stop()
    t2.stop()
    print("Threads started, waiting for them to complete")
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()

    
        