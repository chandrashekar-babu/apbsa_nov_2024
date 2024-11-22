from multiprocessing import Process, current_process
from signal import signal, SIGTERM, SIGUSR1

from time import sleep

def testfn():
    name = current_process().name
    cancel = [False]

    def cleanup(signum, frame):
        print(f"{name}: got terminate ({signum}) signal. Cleaning up...")
        cancel[0] = True

    def show_info(signum, frame):
        print(f"{name}: got SIGUSR1 ({signum}) signal. Cleaning up...")

    signal(SIGTERM, cleanup)
    signal(SIGUSR1, show_info)

    for i in range(20):
        print(f"{name} testfn(): counting {i}")
        sleep(1)
        if cancel[0]:
            break

    print(f"{name}: testfn() exiting...")


if __name__ == '__main__':
    proc = Process(target=testfn)
    proc.start()

    sleep(5)
    #proc.terminate()
    import os
    os.kill(proc.pid, SIGUSR1)

    sleep(2)
    proc.terminate()
