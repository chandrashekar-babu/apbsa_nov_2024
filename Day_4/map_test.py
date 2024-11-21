from time import sleep, time
from concurrent.futures import ThreadPoolExecutor as Executor

def square(x):
    sleep(1)
    return x*x

numbers = [4, 2, 6, 7, 5, 8, 9]

if __name__ == '__main__':
    start = time()
    result = [ square(x) for x in numbers ]
    # result = list(map(square, numbers))
    duration = time() - start
    print(f"result = {result}, duration = {duration}")

    start = time()
    with Executor(max_workers=10) as workers:
        result = list(workers.map(square, numbers))
    duration = time() - start
    print(f"result = {result}, duration = {duration}")
