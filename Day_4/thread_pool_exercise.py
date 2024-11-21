"""
Implement 'thread_pool' module hosting 'ThreadPool'
class that allows us to create a pool of worker threads
waiting on a job-queue for any jobs (functions) to be
submitted.

Implement the ThreadPool class such that the code within
the '__main__' namespace works.


"""
from thread_pool_with_future import ThreadPool

if __name__ == '__main__':

    def foo(x, y):
        print("foo called: x = {}, y = {}".format(x, y))
        return x + y

    def bar(x, y):
        print("bar called: x = {}, y = {}".format(x, y))
        return x * y

    def test(x):
        print("test called: x = {}".format(x))
        return x ** x

    def square(x):
        from time import sleep
        sleep(0.5)
        return x*x

    with ThreadPool(max_workers=10) as pool:
        foo_result = pool.submit(fn=foo, args=(10, 20))
        bar_result = pool.submit(fn=bar, args=("Hello", 10))
        test_result = pool.submit(fn=test, args=(100,))

    print(foo_result.result(), bar_result.result(), test_result.result())

    result = pool.map(square, [2, 5, 6, 3, 8, 6])
