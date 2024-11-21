from queue import Queue
from threading import Thread, Event

class ThreadPool:
    def __init__(self, max_workers):
        self.workers = []
        self.queue = Queue(max_workers)
        self.cancel = Event()
        for _ in range(max_workers):
            t = Thread(target=self.__wait_on_queue)
            self.workers.append(t)            
    

    def __wait_on_queue(self):
        while not self.cancel.isset():
            fn, args, kwargs = self.queue.get()
            if fn is None:
                continue
            fn(*args, **kwargs)

    def start(self):
        self.cancel.clear()
        for worker in self.workers:
            worker.start()

    def shutdown(self):
        self.cancel.set()
        for w in self.workers:
            self.queue.submit((None, None, None))

    def submit(self, fn, args=(), kwargs={}):
        self.queue.put((fn, args, kwargs))

    
