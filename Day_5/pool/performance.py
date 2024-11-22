log = { }

def timeit(f):
    def log_time(*args, **kwargs):
        from time import time
        start = time()
        r = f(*args, **kwargs)
        duration = time() - start
        log[f.func_name] = duration
        return r
    return log_time

def print_log():
    for k, v in log.items(): 
        print k, ": ", v, "seconds"


