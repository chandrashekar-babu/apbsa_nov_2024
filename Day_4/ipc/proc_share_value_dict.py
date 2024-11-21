from multiprocessing import Process
from multiprocessing import Value

from time import sleep

measurements = {
    "cpu": Value("i", 0),
    "mem": Value("i", 0),
    "temperature": Value("i", 0)
}


def update_cpu(m):
    m["cpu"].value = 30


def update_mem(m):
    m["mem"].value = 60


if __name__ == '__main__':

    t1 = Process(target=update_cpu, args=(measurements,))
    t2 = Process(target=update_mem, args=(measurements,))

    t1.start()
    t2.start()
    print(f"Created tasks - {t1} and {t2}")

    t1.join()
    t2.join()
    print("CPU: ", measurements["cpu"].value)
    print("Memory: ", measurements["mem"].value)
    