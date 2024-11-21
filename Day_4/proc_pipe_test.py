
from multiprocessing import Process, Pipe, Event, current_process as current
from random import random
from time import sleep

def sender(outs):
    data = 10, True, {"name": "John"}, [11, 22, 33], None, 6.7
    for d in data:
        print("sender: sending - ", d)
        outs.send(d)
        sleep(random())

def receiver(ins):
    p = current()
    while True:
        d = ins.recv()
        print(f"receiver[{p.name}]: received - {d}")
        print("-" * 40)
        sleep(random())

if __name__ == '__main__':
    ins, outs = Pipe()
    p1 = Process(target=sender, args=(outs,))
    p2 = Process(target=receiver, args=(ins,))
    p3 = Process(target=receiver, args=(ins,))
    p1.start()
    p2.start()
    p3.start()

