from gevent import monkey; monkey.patch_all()
from threading import Thread as Task, current_thread as current, Event
#from multiprocessing import Process as Task, current_process as current, Event
from time import sleep

cancel = Event()
DELAY = 1

def counter():
    t = current()
    
    i = 0
    while not cancel.wait(DELAY):
        print(f"{t.name}: counting {i}")
        i += 1

if __name__ == '__main__':
    workers = []

    for i in range(5):
        w = Task(target=counter)
        w.start()
        print(f"Main: started {w.name}")
        workers.append(w)
    
    sleep(30)
    cancel.set()
    for w in workers:
        w.join()
        print(f"{w.name} finished.")

