from threading import Thread, current_thread as current

def counter(count, delay):
    from time import sleep
    for i in range(count):
        t = current()
        print(f"counter[{t.name}]: counting {i}")
        sleep(delay)

if __name__ == '__main__':
    c1 = Thread(target=counter, name="test-thread", args=(5, 2))
    c2 = Thread(target=counter, name="monitor-thread", kwargs={"count": 10, "delay": 1})
    c3 = Thread(target=counter, name="counter-thread", kwargs=dict(count=10, delay=1))

    c1.start()
    c2.start()
    c3.start()

    counter(10, 0.5)
    print("main: counter complete")
    c1.join()
    print(c1, "completed")
    c2.join()
    print(c2, "completed")
    c3.join()
    print(c3, "completed")

    
