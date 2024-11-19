from threading import Thread
import time

def foo():
    print("this is foo...")

def bar():
    print("this is bar...")

class RunPeriodic(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None, delay=0):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.__delay = delay
        self.__target = target
        self.__args = args
        self.__kwargs = kwargs
        self.__quit = True

    def start(self):
        self.__quit = False
        super().start()

    def stop(self):
        self.__quit = True

    def run(self):
        from time import sleep
        while not self.__quit:
            self.__target(*self.__args, **self.__kwargs)
            sleep(self.__delay)
            
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

    
        