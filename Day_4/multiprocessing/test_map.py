from performance import timeit, print_log

data = range(8000000)


def square(x): return x*x

@timeit
def apply_map(data):
    return map(lambda x: x*x, data)

@timeit
def apply_comprehension(data):
    return [ x*x for x in data ]

@timeit
def apply_for_loop(data):
    b = []
    for i in data:
        b.append(square(i))
    return b

apply_map(data)
apply_comprehension(data)
apply_for_loop(data)

print_log()

