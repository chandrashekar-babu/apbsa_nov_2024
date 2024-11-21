from multiprocessing import Process, Event, Array

from multiprocessing.shared_memory import SharedMemory
from array import array


def writer(buf, r, w):
    w.clear()
    for i, v in enumerate(buf):
        buf[i] = v*v
    w.set()

    r.wait()
    print("Writer: Read back: ", list(buf))

def reader(buf, r, w):
    w.wait()
    print("Reader: buf =", list(buf))
    
    r.clear()
    for i, v in enumerate(buf):
        buf[i] = v // 2
    r.set()


if __name__ == '__main__':
    r = Event()
    w = Event()
    a = Array("i", [2, 5, 3, 8, 9, 12, 7])

    p1 = Process(target=writer, args=(a, r, w))
    p2 = Process(target=reader, args=(a, r, w))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

