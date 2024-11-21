from gevent import monkey; monkey.patch_all()

from threading import Thread as Task
#from multiprocessing import Process as Task
from time import sleep

tasks = []
for _ in range(20):
    t = Task(target=sleep, args=(60,))
    t.start()
    tasks.append(t)

for t in tasks:
    t.join()
