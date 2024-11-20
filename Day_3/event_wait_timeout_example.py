from threading import Thread, Event, current_thread as current
from time import sleep, ctime

DELAY = 10

quit = Event()

def testfn_old():
    t = current()
    while True:
        print(f"[{ctime()}][{t.name}]: sleeping for {DELAY} seconds.")
        sleep(DELAY)
        print(f"[{ctime()}][{t.name}]: woke up.")
        if quit.is_set():
            break

def testfn():
    t = current()
    while True:
        print(f"[{ctime()}][{t.name}]: sleeping for {DELAY} seconds.")
        if quit.wait(timeout=DELAY):
            break
        print(f"[{ctime()}][{t.name}]: woke up.")


def testfn2():
    t = current()
    print(f"[{ctime()}][{t.name}]: started.")
    while not quit.wait(timeout=DELAY):
        print(f"[{ctime()}][{t.name}]: woke up.")
        print(f"[{ctime()}][{t.name}]: sleeping for {DELAY} seconds.")
 


if __name__ == '__main__':
    t = Thread(target=testfn)
    t.start()
    print(f"[{ctime()}][main]: Thread {t.name} started")
    sleep(3)

    print(f"[{ctime()}][main]: Setting quit event")
    quit.set()

    print(f"[{ctime()}][main]: Waiting for thread to end")
    t.join()
    print(f"[{ctime()}][main]: Thread {t.name} finished")


