from multiprocessing import Process, Event

from time import ctime, sleep
from random import random, randint
from sys import stdout

score = {
    "aaa" : 0,
    "bbb" : 0,
    "ccc" : 0
}

update = Event()

def reader(name):
    while True:
        output = """
            ---------------------------------
            %s: %s: current score
            ---------------------------------
            %s
            *********************************
        """ 
        stdout.write(output % (ctime(), name, str(score)))
        stdout.flush()
        update.wait()

def writer():
    while True:
        update.clear()
        sleep(random() * 10)
        score["aaa"] = randint(10, 100)
        score["bbb"] = randint(10, 100)
        score["ccc"] = randint(10, 100)
        update.set()

w = Process(target=writer)

readers = { }

for i in range(5):
    readers[i] = Process(target=reader, args=("Reader %d" % i, ))     
    readers[i].start()

sleep(5)
w.start()







