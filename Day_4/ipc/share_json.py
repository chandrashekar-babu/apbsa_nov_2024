from time import sleep
from multiprocessing import Process, Manager

def foo(data):
    print "In foo: name =", data["name"]
    print "In foo: city =", data["city"]
    data["name"] = "Smith"
    data["city"] = "Kolkatta"

def bar(data):
    sleep(1)
    print "In bar: name =", data["name"]
    print "In bar: city =", data["city"]
    data["name"] = "Jane"
    data["city"] = "Bengaluru"
    print "Bar complete"


import json

m = Manager()
d = m.dict()
d.update(json.load(open("data.json")))

t1 = Process(target=foo, args=(d,))
t2 = Process(target=bar, args=(d,))

t1.start()
t2.start()

t1.join()
t2.join()

print d

