from threading import Thread, Event

class RunPeriodic(Thread):
    def __init__(self, interval, fn, args=(), kwargs={}, *a, **k):
        super().__init__(*a, **k)
        self.sleep_interval = interval
        self.target_fn = fn
        self.fn_args = args
        self.fn_kwargs = kwargs
        self.quit = Event()

    def run(self):
        while not self.quit.wait(self.sleep_interval):
            self.target_fn(*self.fn_args, **self.fn_kwargs)

    def stop(self):
        self.quit.set()

