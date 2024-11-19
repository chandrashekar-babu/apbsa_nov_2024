from threading import Thread
from time import sleep

def testfn():
    for i in range(15):
        print(f"testfn: counting {i}")
        sleep(1)

if __name__ == '__main__':
    t = Thread(target=testfn)
    t.start()
    print(f"In main: thread {t} started...")
    for i in range(5):
        print(f"main: counting {i}")
        sleep(1)

    print("waiting for thread to complete...")
    while t.is_alive():
        print("Waiting...")
        t.join(timeout=1)
        
    print(f"Thread {t.name} finished.")

