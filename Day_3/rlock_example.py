from threading import Thread, RLock, current_thread as current
from time import sleep

stats = {
    "cpu": 0,
    "mem": 0,
    "temp": 0
}

stats_lock = RLock()

def update_cpu_stats():
        with stats_lock:
            stats["cpu"] += 2
        print(f"update_cpu_stats: {stats=}")        

def update_mem_stats():
        with stats_lock:
            stats["mem"] += 2
        print(f"update_mem_stats: {stats=}")        

def update_stats():
        with stats_lock:
            update_cpu_stats()
            update_mem_stats()
        print("update_stats:", stats)

if __name__ == '__main__':
    #update_cpu_stats()
    #update_mem_stats()
    update_stats()


