from threading import Thread
import time

def foo():
    print("this is foo...")

def bar():
    print("this is bar...")

class RunPeriodic:
    def __init__(self, target, *a, args=(), kwargs={}, delay=0, **k):
        self.thread = Thread(*a, target=self.run, **k)
        self.__delay = delay
        self.__target = target
        self.__args = args
        self.__kwargs = kwargs
        self.__quit = True

    def start(self):
        self.__quit = False
        self.thread.start()

    def stop(self):
        self.__quit = True

    def run(self):
        from time import sleep
        while not self.__quit:
            self.__target(*self.__args, **self.__kwargs)
            sleep(self.__delay)

    def join(self):
        self.thread.join()
      
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

    
        