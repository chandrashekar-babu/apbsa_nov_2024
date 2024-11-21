from multiprocessing import Process, Event

from multiprocessing.shared_memory import SharedMemory
from array import array


def writer(shm, r, w):
    #buf = array('i', shm.buf)
    buf = shm.buf
    w.clear()
    for i in range(10):
        buf[i] = i*i
    w.set()

    r.wait()
    print("Writer: Read back: ", list(buf[:10]))

def reader(shm, r, w):
    #buf = array('i', shm.buf)
    buf = shm.buf
    w.wait()
    print("Reader: buf =", list(buf[:10]))
    
    r.clear()
    for i, v in enumerate(buf[:10]):
        buf[i] = v // 2
    r.set()


if __name__ == '__main__':
    r = Event()
    w = Event()
    shm = SharedMemory(name="nums3", create=True, size=4096)
    #a = array("i", shm.buf)

    p1 = Process(target=writer, args=(shm, r, w))
    p2 = Process(target=reader, args=(shm, r, w))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    shm.close()
    shm.unlink()
