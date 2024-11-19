from threading import Thread
from time import sleep

class Counter(Thread):
    def __init__(self, name, count):
        self.__name = name
        self.__count = count
        super().__init__() # Python 3.3+
        # super(Counter, self).__init__()  # Python 3.0 to 3.2
        # Thread.__init__(self) # Works on all versions of Python

    def run(self):
        for i in range(self.__count):
            print(f"Counter[{self.__name}]: {i=}")
            sleep(1)

if __name__ == '__main__':
    c1 = Counter("counter-1", 10)
    c2 = Counter("counter-2", 5)
    c3 = Counter("counter-3", 8)
    c1.start()
    c2.start()
    c3.start()
    
