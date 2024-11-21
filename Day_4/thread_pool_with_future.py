from queue import Queue
from threading import Thread, Event, current_thread

class Future:
    def __init__(self, fn, args=(), kwargs={}):
        self._fn = fn
        self._args = args
        self._kwargs = kwargs
        self._result_status = Event()
        self._result = None
        self.status = "queued"

    def run(self):
        self.status = "inflight"
        self._result_status.clear()
        self._result = self._fn(*self._args, **self._kwargs)
        self._result_status.set()
        self.status = "done"

    def result(self, timeout=None):
        if self._result_status.wait(timeout):
            return self._result


class ThreadPool:
    def __init__(self, max_workers):
        self.workers = []
        self.queue = Queue(max_workers)
        self.cancel = Event()
        for _ in range(max_workers):
            t = Thread(target=self.__wait_on_queue)
            self.workers.append(t)            

    def __wait_on_queue(self):
        while not self.cancel.is_set():
            print(f"{current_thread().name}: waiting on queue")
            job = self.queue.get()
            print(f"{current_thread().name}: fetched job {job}")
            if job is None:
                continue
            job.run() 

    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, et, ev, tb):
        self.shutdown()

    def start(self):
        self.cancel.clear()
        for worker in self.workers:
            worker.start()

    def shutdown(self):
        self.cancel.set()
        for w in self.workers:
            self.queue.put(None)

    def submit(self, fn, args=(), kwargs={}):
        job = Future(fn, args, kwargs)
        self.queue.put(job)
        return job

    
