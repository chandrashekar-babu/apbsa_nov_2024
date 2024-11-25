from gevent import monkey; monkey.patch_all
from time import sleep, time
from concurrent.futures import ThreadPoolExecutor as Executor

nums = [2, 4, 5, 6, 7, 8, 55, 66, 77, 33, 22, 33, 44, 55, 66]

def square(x):
    sleep(1)
    return x*x

if __name__ == '__main__':

    #start = time()
    #result = list(map(square, nums))
    #result = [ square(x) for x in nums ]
    #duration = time() - start
    #print(f"{result=}, {duration=}")

    # For ProcessPoolExecutors, max_workers is generally computed as 
    #  int(num_of_cpus / duty_cycle)
     
    with Executor(max_workers=len(nums)) as workers:
        start = time()
        result = list(workers.map(square, nums))
        duration = time() - start
        print(f"{result=}, {duration=}")
