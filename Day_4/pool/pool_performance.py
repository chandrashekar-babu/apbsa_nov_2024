from performance import timeit, print_log
from multiprocessing import Pool

data = range(800)

def compute(x):
    z = 0
    for i in range(x):
        for j in range(x):
            z += i * j

@timeit
def apply_map(data):
    return map(compute, data)

@timeit
def apply_pool_map(p, data):
    return p.map(compute, data)
    # p.apply_async(compute, data)


apply_map(data)

p = Pool(16)
apply_pool_map(p, data)

print_log()

