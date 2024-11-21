
from multiprocessing import Process, Pipe, Event, current_process as current
from random import random
from time import sleep

def sender(outs):
    data = 10, True, {"name": "John"}, [11, 22, 33], None, 6.7
    for d, o in zip(data, outs):
        o.send(d)
        print("sender: sent", d)


def receiver(ins):
    p = current()
    while True:
        d = ins.recv()
        print(f"receiver[{p.name}]: received - {d}")
        print("-" * 40)

if __name__ == '__main__':
    pipes = [Pipe() for _ in range(5)]

    s = Process(target=sender, args=([p[0] for p in pipes],))
    
    readers = [ Process(target=receiver, args=(pipes[i][1],)) for i in range(5) ]
    for r in readers:
        r.start()

    s.start()
