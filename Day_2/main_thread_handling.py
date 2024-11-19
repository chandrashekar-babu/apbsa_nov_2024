from threading import Thread, current_thread as current
import threading

def counter(count, delay):
    from time import sleep
    t = current()
    if t is threading.main_thread():
        for w in threading.enumerate():
            if w is not t and not w.daemon:
                print(f"{t.name}: waiting for {w.name} to complete.")
                w.join()
                print(f"{t.name}: {w.name} finished.")
    else:
        for i in range(count):
            print(f"counter[{t.name}]: counting {i}")
            sleep(delay)

if __name__ == '__main__':
    c1 = Thread(target=counter, name="test-thread", args=(30, 0.5), daemon=True)
    c2 = Thread(target=counter, name="monitor-thread", kwargs={"count": 10, "delay": 1})   
    c1.start()
    c2.start()
    counter(0, 0)

